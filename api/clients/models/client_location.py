# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from clients.models import Client
from locations.models import ZipCode

class ClientLocation(BaseModel):
    id          = models.IntegerField(primary_key=True)
    client      = models.ForeignKey(Client, related_name='locations')
    zip_code    = models.ForeignKey(ZipCode, related_name='client_locations')
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_locations'
        verbose_name = 'Client Location'
        verbose_name_plural = 'Client Locations'
