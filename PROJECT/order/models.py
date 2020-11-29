from django.db import models

# from django.contrib.auth import get_user_model
#  from PROJECT.users.models import User
# from PROJECT.PROJECT.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from PROJECT.product.models import Product


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    products_ordered = models.ManyToManyField(to=Product, through='OrderUnit')
    ordered = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=31)

    def __str__(self):
        return self.User.email


class OrderUnit(models.Model):

    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()

    def __str__(self):
        return '{} pcs of {} by {}'.format(self.quantity, self.product, self.order.name)
