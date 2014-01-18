# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from zip_code import ZipCode

class Location(BaseModel):
    id          = models.IntegerField(primary_key=True)
    zip_code    = models.ForeignKey(ZipCode, related_name='locations')
    city        = models.CharField(max_length=255)
    state       = models.CharField(max_length=255)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'locations'
        db_table = 'locations'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
