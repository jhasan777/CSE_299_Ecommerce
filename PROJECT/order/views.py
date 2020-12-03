from django.shortcuts import render

# Create your views here.
from django.contrib.sessions.models import Session
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, OrderUnit
from .serializers import OrderListSerializer, OrderSerializer, OrderDetailSerializer, DeliveryInfoSerializer


from .models import DeliveryInfo
from .service import DeliveryInfoService


class DeliveryInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        try:
            deliveryinfo = user.deliveryinfo
        except DeliveryInfo.DoesNotExist:
            return Response({})

        return Response(DeliveryInfoSerializer(deliveryinfo).data)

    def post(self, request):
        serializer = DeliveryInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        DeliveryInfoService.delete_by_user(request.user)

        serializer.save(user=request.user)

        return Response(status=status.HTTP_201_CREATED)


class OrderView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        user = request.user

        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        queryset = Order.objects.filter(user=user)
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        if not bool(request.user.is_anonymous):
            cart_units = request.user.cart_units.all()
            data['user'] = request.user

            DeliveryInfoService.delete_by_user(request.user)
            DeliveryInfo.objects.create(**data)
        else:
            if request.session.session_key is None:
                request.session.save()

            cart_units = Session.objects.get(session_key=request.session.session_key).cart_units.all()
            data['user'] = None

        if cart_units.count() == 0:
            raise serializers.ValidationError('Cart is empty, nothing to order')

        order = Order.objects.create(**data)

        for cart_unit in cart_units:
            if cart_unit.unit.num_in_stock < cart_unit.quantity:
                raise serializers.ValidationError(
                    'Not enough units in stock: {}'.format(cart_unit.unit.sku)
                )

        for cart_unit in cart_units:
            unit = cart_unit.unit

            OrderUnit.objects.create(
                order=order,
                quantity=cart_unit.quantity,
                unit=unit,
                unit_price=unit.price
            )

            unit.num_in_stock -= cart_unit.quantity
            unit.save()

            # Clear cart
            cart_unit.delete()

        return Response(OrderDetailSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        user = request.user
        order = Order.objects.get(pk=pk)

        if user.id != order.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)
