from django.db import models

from common.models import BaseModel
from user.models import User


class ProductType(BaseModel):
    name = models.CharField(max_length=255)


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)
    latitude = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)
    location = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.CharField(max_length=200, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='fresh')
