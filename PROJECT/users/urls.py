from django.urls import include, path
from rest_framework import routers
from . import views


Userrouter = routers.DefaultRouter()
#
Userrouter.register(r'Users', views.UserViewSet)


urlpatterns = [
    path('rest-auth/', include('rest_framework.urls', namespace='rest_framework')), ## rest-auth urls
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

#### REST API VIEWS URL
#    path('', views.UserViewSet.as_view()),  ## user view urls

    path('', include(Userrouter.urls)),




]

