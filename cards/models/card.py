from django.db import models

from core.models import BaseModel


class Card(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'cards'
        db_table = 'cards'
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
