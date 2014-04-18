# Django
from django.db import models

# Local Apps
from django.db.models.signals import post_save
from core.models import BaseModel
from clients.models import Client
from locations.models import Location

class ClientLocation(BaseModel):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='locations')
    location = models.ForeignKey(Location, related_name='client_locations')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_locations'
        verbose_name = 'Client Location'
        verbose_name_plural = 'Client Locations'


def client_location_post_save_handler(sender, instance, **kwargs):
    from clients.api.resources import ClientLocationList

    # bust the cache on the ClientLocationList
    client_location_list = ClientLocationList()
    client_location_list.bust_cache()

post_save.connect(client_location_post_save_handler, sender=ClientLocation)
