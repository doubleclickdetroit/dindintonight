from autoslug import AutoSlugField
from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class Franchise(BaseModel):
    id = models.AutoField(primary_key=True)
    owner = models.OneToOneField('users.User', related_name='franchise_owners')
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'franchises'
        db_table = 'franchises'
        verbose_name = 'Franchise'
        verbose_name_plural = 'Franchises'

    def __unicode__(self):
        return '{0} {1}'.format(self.owner.first_name, self.owner.last_name)


def franchise_post_save_handler(sender, instance, **kwargs):
    pass

post_save.connect(franchise_post_save_handler, sender=Franchise)
