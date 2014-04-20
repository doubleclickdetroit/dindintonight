from django.db import models
from core.models import BaseModel
from users.models import User
from locations.models import Location


class UserLocation(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='locations')
    location = models.ForeignKey(Location, related_name='user_locations')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'users'
        db_table = 'user_locations'
        verbose_name = 'User Location'
        verbose_name_plural = 'User Locations'
