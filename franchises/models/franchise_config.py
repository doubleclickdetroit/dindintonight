from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class FranchiseConfig(BaseModel):
    id = models.AutoField(primary_key=True)
    franchise = models.OneToOneField('franchises.Franchise', related_name='config')
    css_path = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'franchises'
        db_table = 'franchise_configs'
        verbose_name = 'Franchise Config'
        verbose_name_plural = 'Franchise Configs'

    def __unicode__(self):
        return 'Config for {0}'.format(self.franchise.name)


def franchise_config_post_save_handler(sender, instance, **kwargs):
    pass

post_save.connect(franchise_config_post_save_handler, sender=FranchiseConfig)
