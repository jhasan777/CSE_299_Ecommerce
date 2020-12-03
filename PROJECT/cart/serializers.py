from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from PROJECT.product.models import Product
from PROJECT.order.models import OrderUnit


from PROJECT.product.serializers import ProductForOrderDetail


class CartUnitSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(default=1, min_value=1)
    product = ProductForOrderDetail(read_only=True)

    class Meta:
        model = OrderUnit
        fields = ('slug', 'quantity', 'product')

    def validate(self, data):
        slug = data['slug']
        quantity = data['quantity']

        try:
            product = Product.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Product does not exist')

        if product.num_in_stock < quantity:
            raise serializers.ValidationError('There are not enough units in stock')

        return data
