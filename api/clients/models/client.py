# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel

class Client(BaseModel):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
