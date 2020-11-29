
from rest_framework import serializers

from .models import Product, Rating, Review, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag

    def to_representation(self, instance):
        return instance.name


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'user', 'product', 'comment')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id', 'user', 'product', 'rating')


class ProductListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        many=True,
        read_only=True,
        source='tag_set'
    )
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'price', 'discount_price', 'tags', 'num_in_stock', 'image')

    def get_images(self, obj):
        images = obj.productimage_set.all()

        if images.exists():
            return [image.image.url for image in images.all()]
        else:
            return []




class ProductForOrderDetail(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('title', 'image', 'id', 'price', 'num_in_stock')

    def get_image(self, obj):
        image = obj.productimage_set.order_by('-is_main').first()

        if image is None:
            return None

        return image.image.url

#########################################################################


# class ProductSerializer(ProductListSerializer):
#     units = UnitSerializer(
#         many=True,
#         read_only=True,
#         source='unit_set'
#     )
#
#     class Meta:
#         model = Product
#         fields = ('id', 'title', 'tags', 'description', 'units')
#

