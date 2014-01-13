# Django
from django.db import models

# 3rd party
from core.models import BaseModel
from locations.models import Location

class Drop(BaseModel):
    id              = models.AutoField(primary_key=True)
    location        = models.ForeignKey(Location)
    date_and_time   = models.DateTimeField()
    timezone        = models.CharField(max_length=255)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'drops'
        db_table = 'drops'
        verbose_name = 'Drop'
        verbose_name_plural = 'Drops'
