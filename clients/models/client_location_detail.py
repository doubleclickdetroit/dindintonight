from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class ClientLocationDetail(BaseModel):
    id = models.AutoField(primary_key=True)
    client_location = models.OneToOneField('clients.ClientLocation', related_name='details')
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    phone_number = models.CharField(max_length=20, blank=True)
    manager_name = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_location_details'
        verbose_name = 'Client Location Detail'
        verbose_name_plural = 'Client Location Details'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.pk, self.address1, self.manager_name)


def client_location_detail_post_save_handler(sender, instance, **kwargs):
    from clients.api import ClientLocationSearchList

    # bust the cache on the ClientLocationSearchList
    client_location_search_list = ClientLocationSearchList()
    client_location_search_list.bust_cache()

post_save.connect(client_location_detail_post_save_handler, sender=ClientLocationDetail)
