from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):  # ALL USER DATA VIEW
    class Meta:
        model = models.User
        fields = ('id', 'email', 'name', 'last_login', 'date_joined')
