# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from vendors.models import Vendor
from users.models import User

class VendorUser(BaseModel):
    id          = models.IntegerField(primary_key=True)
    vendor      = models.ForeignKey(Vendor, related_name='users')
    user        = models.ForeignKey(User, related_name='vendors')
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'vendors'
        db_table = 'vendor_users'
        verbose_name = 'Vendor User'
        verbose_name_plural = 'Vendor Users'
