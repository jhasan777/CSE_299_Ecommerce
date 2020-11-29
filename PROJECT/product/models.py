from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    tag_set = models.ManyToManyField(to=Tag)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    num_in_stock = models.PositiveIntegerField(default=5)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

###############################

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

############################################################################


class ProductImage(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)

    class Meta:
        ordering = ['image']

    def __str__(self):
        if Product is not None:
            product_title = Product.title
        else:
            product_title = 'No unit assigned'

        return '{}: {}'.format(product_title, self.image.name)

    def delete(self, *args, **kwargs):
        self.image.delete()

        super(ProductImage, self).delete(*args, **kwargs)

############################################################################


class Rating(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField()

    class Meta:
        ordering = ['product']

    def __str__(self):
        return self.product


class Review(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024, null=True, blank=False)
    sentiment = models.FloatField

    class Meta:
        ordering = ['product']

    def __str__(self):
        return self.product
