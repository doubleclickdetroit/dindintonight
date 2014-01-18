# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from clients.models import Client

class ClientHost(BaseModel):
    id          = models.IntegerField(primary_key=True)
    client      = models.ForeignKey(Client, related_name='hosts')
    value       = models.CharField(max_length=255)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_hosts'
        verbose_name = 'Client Host'
        verbose_name_plural = 'Client Hosts'
