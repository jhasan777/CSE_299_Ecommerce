# from django.shortcuts import render

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Product, Review, Rating, Tag
from .serializers import ProductListSerializer, RatingSerializer, ReviewSerializer, TagSerializer


# from rest_framework.decorators import action
# from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer





class ProductSetPagination(PageNumberPagination):
    page_size = 32

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'page': self.page.number,
                'has_prev': self.page.has_previous(),
                'has_next': self.page.has_next(),
            },
            'data': data
        })


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = ProductSetPagination

    def get_queryset(self):
        queryset = Product.objects.all()

        q = self.request.query_params.get('q', None)
        tags = self.request.query_params.get('tags')
        in_stock = self.request.query_params.get('in_stock', None)

        if q is not None:
            queryset = queryset.filter(title__icontains=q)

        if tags:
            tags = tags.split(',')

            for tag in tags:
                queryset = queryset.filter(tag_set__name__iexact=tag).distinct()

        if in_stock == '1':
            queryset = queryset.filter(unit__num_in_stock__gt=0).distinct()

        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


#################################################################
#   NON API VIEWS

