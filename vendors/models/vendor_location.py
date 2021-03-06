from django.db import models
from django.db.models.signals import post_save

from core.models import BaseModel


class VendorLocation(BaseModel):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey('vendors.Vendor', related_name='locations')
    location = models.ForeignKey('locations.Location')
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'vendors'
        db_table = 'vendor_locations'
        verbose_name = 'Vendor Location'
        verbose_name_plural = 'Vendor Locations'

    def __unicode__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.address1, self.address2,
                                           self.address3, self.location.city, self.location.state,
                                           self.location.zip_code)


def vendor_location_post_save_handler(sender, instance, **kwargs):
    from vendors.api import VendorLocationList
    # bust the cache on the VendorLocationList
    vendor_location_list = VendorLocationList()
    vendor_location_list.bust_cache()


post_save.connect(vendor_location_post_save_handler, sender=VendorLocation)
