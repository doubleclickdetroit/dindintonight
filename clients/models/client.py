from django.db import models
from django.db.models.signals import post_save

from core.models import BaseModel


class Client(BaseModel):
    id = models.AutoField(primary_key=True)
    franchise = models.ForeignKey('franchises.Franchise', related_name='clients')
    users = models.ManyToManyField('users.User', through='clients.ClientUser', related_name='clients')
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __unicode__(self):
        return '{0} - {1}'.format(self.pk, self.name)


def client_post_save_handler(sender, instance, **kwargs):
    from clients.api import ClientList

    # bust the cache on the ClientList
    client_list = ClientList()
    client_list.bust_cache()

post_save.connect(client_post_save_handler, sender=Client)
