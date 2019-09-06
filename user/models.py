from django.db import models

from common.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=200, default="")
    user_type = models.CharField(max_length=100, default='farmer')
    phone = models.CharField(max_length=10)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)
    latitude = models.DecimalField(max_digits=8, decimal_places=3, default=0.0)
