# Django
from django.db import models

# 3rd party
from core.models import BaseModel

class Location(BaseModel):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    address         = models.CharField(max_length=255)
    city            = models.CharField(max_length=255)
    state           = models.CharField(max_length=255)
    zip             = models.CharField(max_length=255)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'locations'
        db_table = 'locations'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
