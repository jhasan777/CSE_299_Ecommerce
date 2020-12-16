from django.conf.urls import url
from django.urls import path,include

from .views import TagViewSet, RatingViewSet, ReviewViewSet, ProductListView, ProductDetailView



review_list = ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
review_detail = ReviewViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

rating_list = RatingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
rating_detail = RatingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

tag_list = TagViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
tag_detail = TagViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



urlpatterns = [
    path('tags/', tag_list, name='tag_list'),
    path('tags/<int:pk>/', tag_detail, name='tag_detail'),

    path('product/', ProductListView, name='product_list'),
    path('products/<slug:slug>/', ProductDetailView, name='product_detail'),


    path('ratings/', rating_list, name='rating_list'),
    path('ratings/<int:pk>/', rating_detail, name='rating_detail'),

    path('reviews/', rating_list, name='rating_list'),
    path('reviews/<int:pk>/', rating_detail, name='rating_detail'),

]               ###CHANGE TO SLUG

                ####ADD Routers for review
                     #/rating

