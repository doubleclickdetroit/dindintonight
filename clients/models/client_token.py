from django.db import models
from core.models import BaseModel


class ClientToken(BaseModel):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey('clients.Client', related_name='tokens')
    value = models.CharField(max_length=36)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_tokens'
        verbose_name = 'Client Token'
        verbose_name_plural = 'Client Tokens'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.pk, self.client.name, self.value)
