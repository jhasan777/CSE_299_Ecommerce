from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from . import models
from . import serializers

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer