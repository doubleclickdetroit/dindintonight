from django.db import models

from core.models import BaseModel


class VendorUser(BaseModel):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey('vendors.Vendor', related_name='users')
    user = models.ForeignKey('users.User', related_name='vendors')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'vendors'
        db_table = 'vendor_users'
        verbose_name = 'Vendor User'
        verbose_name_plural = 'Vendor Users'


# def client_location_post_save_handler(sender, instance, **kwargs):
#
#     # bust the cache on the ClientLocationList
#     client_location_list = ClientLocationList()
#     client_location_list.bust_cache()
#
#
# post_save.connect(client_location_post_save_handler, sender=ClientLocation)
