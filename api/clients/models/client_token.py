# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from clients.models import Client

class ClientToken(BaseModel):
    id          = models.IntegerField(primary_key=True)
    client      = models.ForeignKey(Client, related_name='tokens')
    value       = models.CharField(max_length=36)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_tokens'
        verbose_name = 'Client Token'
        verbose_name_plural = 'Client Tokens'
