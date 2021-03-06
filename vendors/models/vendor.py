from django.db import models

from core.models import BaseModel


class Vendor(BaseModel):
    id = models.AutoField(primary_key=True)
    franchise = models.ForeignKey('franchises.Franchise', related_name='vendors')
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'vendors'
        db_table = 'vendors'
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __unicode__(self):
        return self.name
