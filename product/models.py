from django.db import models

from common.models import BaseModel
from user.models import User


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)
    latitude = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)
    location = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
