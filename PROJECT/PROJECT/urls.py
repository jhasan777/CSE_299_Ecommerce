"""PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


## from *unicorns*.views import *UnicornViewSet* --- import views for router

#   router = DefaultRouter()
#   router.register('unicorn', UnicornViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')), #####OAUTH2 provider
    #  path('bkash/', include('bkash.urls')),
    path('accounts/', include('allauth.urls')),  ###ALLAUTH PATH





    #### API's

    path('api/users/', include('users.urls')),  #users api urls|||includes /rest-auth
    path('api/products/', include('product.urls')),


    path('/store', include(#'product.urls')),
    path('', ),


]
