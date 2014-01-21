# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel

class Location(BaseModel):
    id          = models.AutoField(primary_key=True)
    city        = models.CharField(max_length=255)
    state       = models.CharField(max_length=255)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'locations'
        db_table = 'locations'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __unicode__(self):
        return '%s, %s' % (self.city, self.state)
