from django.db import models
from django.db.models.signals import post_save

from core.models import BaseModel


class ClientLocation(BaseModel):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey('clients.Client', related_name='locations')
    location = models.ForeignKey('locations.Location', related_name='client_locations')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_locations'
        verbose_name = 'Client Location'
        verbose_name_plural = 'Client Locations'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.pk, self.client.name, self.location.zip_code)


def client_location_post_save_handler(sender, instance, **kwargs):
    from clients.api import ClientLocationList, ClientLocationSearchList

    # bust the cache on the ClientLocationList
    client_location_list = ClientLocationList()
    client_location_list.bust_cache()

    # bust the cache on the ClientLocationSearchList
    client_location_search_list = ClientLocationSearchList()
    client_location_search_list.bust_cache()

post_save.connect(client_location_post_save_handler, sender=ClientLocation)
