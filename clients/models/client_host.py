from django.db import models

from core.models import BaseModel


class ClientHost(BaseModel):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey('clients.Client', related_name='hosts')
    value = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_hosts'
        verbose_name = 'Client Host'
        verbose_name_plural = 'Client Hosts'

    def __unicode__(self):
        return '{0} - {1} {2}'.format(self.pk, self.client.name, self.value)
