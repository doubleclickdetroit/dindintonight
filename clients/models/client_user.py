from django.db import models
from core.models import BaseModel


class ClientUser(BaseModel):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey('clients.Client')
    user = models.ForeignKey('users.User')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_users'
        verbose_name = 'Client User'
        verbose_name_plural = 'Client Users'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.pk, self.client.name, self.user)
