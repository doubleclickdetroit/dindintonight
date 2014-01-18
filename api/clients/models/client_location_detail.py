# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from clients.models import ClientLocation

class ClientLocationDetail(BaseModel):
    id              = models.IntegerField(primary_key=True)
    client_location = models.ForeignKey(ClientLocation, related_name='details')
    address1        = models.CharField(max_length=255, blank=True)
    address2        = models.CharField(max_length=255, blank=True)
    address3        = models.CharField(max_length=255, blank=True)
    phone_number    = models.CharField(max_length=20)
    manager_name    = models.CharField(max_length=255)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_location_details'
        verbose_name = 'Client Location Detail'
        verbose_name_plural = 'Client Location Details'
