# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel

class Location(BaseModel):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'locations'
        db_table = 'locations'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __unicode__(self):
        return '%s, %s, %s' % (self.city, self.state, self.zip_code)
