# Django
from django.db import models

# 3rd party
from core.models import BaseModel
from locations.models import Location

class Address(BaseModel):
    id              = models.AutoField(primary_key=True)
    location        = models.ForeignKey(Location, related_name='location_addresses')
    address         = models.TextField()
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'addresses'
        db_table = 'addresses'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
