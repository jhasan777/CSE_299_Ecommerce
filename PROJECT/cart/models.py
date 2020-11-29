from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from PROJECT.product.models import Product
# Create your models here.


class CartUnit(models.Model):
    user = models.ForeignKey(to=get_user_model(), null=True, on_delete=models.CASCADE, related_name='cart_units')
    session = models.ForeignKey(to=Session, null=True, on_delete=models.CASCADE, related_name='cart_units')
    item = models.ForeignKey(to=Product)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{} unit(s) of {}'.format(self.quantity, self.item)

