# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from vendors.models import VendorLocation

class Meal(BaseModel):
    id                  = models.IntegerField(primary_key=True)
    vendor_location     = models.ForeignKey(VendorLocation, related_name='meals')
    name                = models.CharField(max_length=255)
    description         = models.CharField(max_length=45)
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    available_starting  = models.DateTimeField(blank=True, null=True)
    available_ending    = models.DateTimeField(blank=True, null=True)
    is_deleted          = models.BooleanField(default=False, db_index=True)
    created             = models.DateTimeField(auto_now_add=True)
    modified            = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'meals'
        db_table = 'meals'
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'
