
from rest_framework import serializers
from .models import Order, OrderUnit
from PROJECT.product.serializers import ProductForOrderDetail




class OrderUnitSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = OrderUnit
        fields = ('quantity', 'product')

    def get_product(self, obj):
        data = ProductForOrderDetail(obj.unit).data

        # Use the price that was at the moment of purchase instead of current price.
        data['price'] = obj.unit_price

        return data






class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('name', 'address', 'phone')



class OrderListSerializer(serializers.ModelSerializer):
    product_num = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'created_at', 'product_num')

    def get_product_num(self, obj):
        return obj.items_ordered.count()


class OrderDetailSerializer(serializers.ModelSerializer):
    products = OrderUnitSerializer(
        many=True,
        read_only=True,
        source='orderunit_set'
    )

    class Meta:
        model = Order
        fields = ('id', 'created_at', 'name', 'address', 'phone', 'products')


