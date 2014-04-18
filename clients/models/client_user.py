# Django
from django.db import models

# Local Apps
from core.models import BaseModel
from clients.models import Client
from users.models import User

class ClientUser(BaseModel):
    id = models.AutoField(primary_key=True)
    client = models.OneToOneField(Client, related_name='users')
    user = models.OneToOneField(User, related_name='clients')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_users'
        verbose_name = 'Client User'
        verbose_name_plural = 'Client Users'
