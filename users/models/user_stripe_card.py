from django.db import models
from django.db.models.signals import post_save
from core.models import BaseModel


class UserStripeCard(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', related_name='cards')
    card_id = models.CharField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=512, blank=True)
    last4 = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    expiration_month = models.CharField(max_length=2)
    expiration_year = models.CharField(max_length=4)
    fingerprint = models.CharField(max_length=255)
    country = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'users'
        db_table = 'user_stripe_cards'
        verbose_name = 'User Stripe Cards'
        verbose_name_plural = 'User Stripe Cards'


def user_stripe_card_post_save_handler(sender, instance, **kwargs):
    from stripe_api.api import CardList

    # bust the cache on the CardList
    card_list = CardList()
    card_list.bust_cache()

post_save.connect(user_stripe_card_post_save_handler, sender=UserStripeCard)
