"""farmer_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

import user.views as user
import product.views as product

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/login/', user.login),
    url(r'^api/v1/update-user/(?P<user_id>\d+)', user.update_user),
    url(r'^api/v1/user/?(?P<user_id>[0-9]*)$', user.get_user),
    url(r'^api/v1/product', include('product.urls')),
    url(r'^api/v1/add-product-type', product.add_product_type),
    url(r'^api/v1/get-product-type', product.get_product_type),
    url(r'^api/v1/get-all-merchants', user.get_merchants),
]
