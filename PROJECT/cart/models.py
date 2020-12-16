from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from product.models import Product

# Create your models here.


class CartUnit(models.Model):
    user = models.ForeignKey(to=get_user_model(), null=True, on_delete=models.CASCADE, related_name='cart_units')   #related name helps reverse relation calls, used in our views
    session = models.ForeignKey(to=Session, null=True, on_delete=models.CASCADE, related_name='cart_units')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{} unit(s) of {}'.format(self.quantity, self.product)

