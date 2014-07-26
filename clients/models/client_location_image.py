from django.db import models
from django.db.models.signals import post_save

from core.models import BaseModel


class ClientLocationImage(BaseModel):
    id = models.AutoField(primary_key=True)
    client_location = models.ForeignKey('clients.ClientLocation', related_name='images')
    name = models.CharField(max_length=125, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    location = models.CharField(max_length=2048, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_location_images'
        verbose_name = 'Client Location Image'
        verbose_name_plural = 'Client Location Images'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.pk, self.client_location.client.name, self.name)


def client_location_image_post_save_handler(sender, instance, **kwargs):
    from clients.api import ClientLocationSearchList

    # bust the cache on the ClientLocationSearchList
    client_location_search_list = ClientLocationSearchList()
    client_location_search_list.bust_cache()

post_save.connect(client_location_image_post_save_handler, sender=ClientLocationImage)
