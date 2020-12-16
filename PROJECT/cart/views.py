from django.shortcuts import render

# Create your views here.
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import CartUnit
from .serializers import CartUnitSerializer
from product.models import Product



class CartView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        if not bool(request.user.is_anonymous):
            cart_units = request.user.cart_units.all()
        else:
            if request.session.session_key is None:
                request.session.save()

            cart_units = Session.objects.get(session_key=request.session.session_key).cart_units.all()

        return Response(CartUnitSerializer(cart_units.order_by('product__slug'), many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartUnitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        product = Product.objects.get(slug=data['slug'])

        cart_unit_data = {
            'product': product,
            'user': None,
            'session': None
        }

        if not bool(request.user.is_anonymous):
            cart_unit_data['user'] = request.user
        else:
            if request.session.session_key is None:
                request.session.save()

            cart_unit_data['session'] = Session.objects.get(session_key=request.session.session_key)

        cart_unit = CartUnit.objects.filter(**cart_unit_data).first()

        if cart_unit is None:
            cart_unit = CartUnit(**cart_unit_data)

        cart_unit.quantity = data['quantity']
        cart_unit.save()

        return Response(status=status.HTTP_201_CREATED)


class CartUnitView(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, slug=None):
        if not bool(request.user.is_anonymous):
            cart_units = request.user.cart_units.all()
        else:
            if request.session.session_key is None:
                request.session.save()

            cart_units = Session.objects.get(session_key=request.session.session_key).cart_units.all()

        cart_unit = cart_units.filter(product__slug=slug).first()

        if cart_unit is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        cart_unit.delete()

        return Response(status=status.HTTP_200_OK)
