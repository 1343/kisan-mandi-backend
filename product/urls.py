"""This file contains endpoints for industry table"""
from django.conf.urls import url

from product import views

urlpatterns = [
    url(r'/?(?P<prod_id>[0-9]*)$', views.route),
]
