# Django
from django.db import models

# 3rd party
from core.models import BaseModel

class Meal(BaseModel):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    description     = models.TextField()
    image           = models.CharField(max_length=255)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'meals'
        db_table = 'meals'
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'
