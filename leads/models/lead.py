from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class Lead(BaseModel):
    id = models.AutoField(primary_key=True)
    franchise = models.ForeignKey('franchises.Franchise', related_name='leads')
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'leads'
        db_table = 'leads'
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __unicode__(self):
        return '{0} - {1} - {2} - {3}'.format(self.pk, self.first_name, self.last_name, self.email)


def lead_post_save_handler(sender, instance, **kwargs):
    from users.models import User
    # if the lead exists as a User then we will delete the lead
    if User.objects.filter(email=instance.email).count() > 0:
        instance.delete()

post_save.connect(lead_post_save_handler, sender=Lead)
