# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel

class ZipCode(BaseModel):
    id          = models.IntegerField(primary_key=True)
    value       = models.CharField(unique=True, max_length=50)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'locations'
        db_table = 'zip_codes'
        verbose_name = 'Zip Code'
        verbose_name_plural = 'Zip Codes'
