# Django
from django.db import models

# 3rd party
from core.models import BaseModel
from .drop import Drop
from meals.models import Meal

class DropMeal(BaseModel):
    id              = models.AutoField(primary_key=True)
    drop            = models.ForeignKey(Drop)
    meal            = models.ForeignKey(Meal)
    quantity        = models.IntegerField()
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'drops'
        db_table = 'drop_meals'
        verbose_name = 'Drop Meal'
        verbose_name_plural = 'Drop Meals'
