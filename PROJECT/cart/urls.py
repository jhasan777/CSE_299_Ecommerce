from django.conf.urls import url

from cart.views import CartView, CartUnitView


# Userrouter = routers.DefaultRouter()
# #
# Userrouter.register(r'Users', views.UserViewSet)
#
# path('', include(Userrouter.urls)),




urlpatterns = [
    url(r'^cart/$',                          CartView.as_view(), name='cart'),
    url(r'^cart/(?P<sku>[A-Za-z\-_0-9]+)/$', CartUnitView.as_view(), name='cart-unit'),
]
