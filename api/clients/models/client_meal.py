# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from clients.models import Client
from meals.models import Meal

class ClientMeal(BaseModel):
    id          = models.IntegerField(primary_key=True)
    client      = models.ForeignKey(Client, related_name='meals')
    meal        = models.ForeignKey(Meal, related_name='clients')
    is_enabled  = models.BooleanField(default=True, db_index=True)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_meals'
        verbose_name = 'Client Meal'
        verbose_name_plural = 'Client Meals'
