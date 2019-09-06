from django.db import models

# Create your models here.
from django.utils import timezone


class BaseModel(models.Model):
    """This class contains common fields in all other classes"""
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        """This class instructs django not to create separate table for \
        this model and make it abstract
        """
        abstract = True