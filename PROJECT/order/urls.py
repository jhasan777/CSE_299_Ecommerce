from django.conf.urls import url

from order.views import OrderView, OrderDetailView,DeliveryInfoView

# Userrouter = routers.DefaultRouter()
# #
# Userrouter.register(r'Users', views.UserViewSet)
#
# path('', include(Userrouter.urls)),




urlpatterns = [
    url(r'^orders/$',                OrderView.as_view(), name='order-list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', OrderDetailView.as_view(), name='order-detail'),
    url(r'^deliveryinfo/$', DeliveryInfoView.as_view(), name='delivery-info'),
]
