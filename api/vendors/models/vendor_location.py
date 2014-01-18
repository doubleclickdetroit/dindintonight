# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from vendors.models import Vendor
from locations.models import ZipCode

class VendorLocation(BaseModel):
    id          = models.IntegerField(primary_key=True)
    vendor      = models.ForeignKey(Vendor, related_name='locations')
    zip_code    = models.ForeignKey(ZipCode)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'vendors'
        db_table = 'vendor_locations'
        verbose_name = 'Vendor Location'
        verbose_name_plural = 'Vendor Locations'
