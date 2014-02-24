# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from clients.models import ClientLocation
from meals.models import Meal

class ClientLocationMeal(BaseModel):
    id = models.AutoField(primary_key=True)
    client_location = models.ForeignKey(ClientLocation, related_name='meals')
    meal = models.ForeignKey(Meal, related_name='clients')
    is_enabled = models.BooleanField(default=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_location_meals'
        verbose_name = 'Client Location Meal'
        verbose_name_plural = 'Client Location Meals'
