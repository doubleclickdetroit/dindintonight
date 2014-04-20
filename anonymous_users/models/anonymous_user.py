from django.db import models
from core.models import BaseModel


class AnonymousUser(BaseModel):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey('locations.Location', related_name='anonymous_users')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'anonymous_users'
        db_table = 'anonymous_users'
        verbose_name = 'Anonymous User'
        verbose_name_plural = 'Anonymous Users'
