from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class Location(BaseModel):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, db_index=True)
    state = models.CharField(max_length=255, db_index=True)
    zip_code = models.CharField(max_length=50, db_index=True)
    latitude = models.CharField(max_length=50, db_index=True)
    longitude = models.CharField(max_length=50, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    index_together = ['city', 'state']

    class Meta:
        app_label = 'locations'
        db_table = 'locations'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __unicode__(self):
        return '%s, %s, %s' % (self.city, self.state, self.zip_code)


def location_post_save_handler(sender, instance, **kwargs):
    from locations.api import LocationList

    # bust the cache on the LocationList
    location_list = LocationList()
    location_list.bust_cache()

post_save.connect(location_post_save_handler, sender=Location)
