from django.contrib import admin
from .models import Product, Rating, Review, Tag, ProductImage
# Register your models here.

admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(ProductImage)