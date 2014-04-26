from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class UserLocation(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', related_name='locations')
    location = models.ForeignKey('locations.Location', related_name='user_locations')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'users'
        db_table = 'user_locations'
        verbose_name = 'User Location'
        verbose_name_plural = 'User Locations'


def user_location_post_save_handler(sender, instance, **kwargs):
    from users.api import UserLocationList

    # bust the cache on the ClientLocationList
    user_location_list = UserLocationList()
    user_location_list.bust_cache()

post_save.connect(user_location_post_save_handler, sender=UserLocation)
