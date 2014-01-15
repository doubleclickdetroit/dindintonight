# Django
from django.db import models

# 3rd party
from core.models import BaseModel
from .location import Location
from meals.models import Meal

class LocationMeal(BaseModel):
    id              = models.AutoField(primary_key=True)
    location        = models.ForeignKey(Location)
    meal            = models.ForeignKey(Meal)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'locations'
        db_table = 'locations_meals'
        verbose_name = 'Location Meal'
        verbose_name_plural = 'Locations Meals'
