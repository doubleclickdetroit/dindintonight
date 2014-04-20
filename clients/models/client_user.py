from django.db import models
from core.models import BaseModel


class ClientUser(BaseModel):
    id = models.AutoField(primary_key=True)
    client = models.OneToOneField('clients.Client', related_name='users')
    user = models.OneToOneField('users.User', related_name='clients')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_users'
        verbose_name = 'Client User'
        verbose_name_plural = 'Client Users'
