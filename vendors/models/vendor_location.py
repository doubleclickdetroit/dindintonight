# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from vendors.models import Vendor
from locations.models import Location

class VendorLocation(BaseModel):
    id          = models.AutoField(primary_key=True)
    vendor      = models.ForeignKey(Vendor, related_name='locations')
    location    = models.ForeignKey(Location)
    address1    = models.CharField(max_length=255)
    address2    = models.CharField(max_length=255)
    address3    = models.CharField(max_length=255)
    manager     = models.CharField(max_length=255)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'vendors'
        db_table = 'vendor_locations'
        verbose_name = 'Vendor Location'
        verbose_name_plural = 'Vendor Locations'

    def __unicode__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.address1, self.address2,
            self.address3, self.location.city, self.location.state,
            self.location.zip_code)
