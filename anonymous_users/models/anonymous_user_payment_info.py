from django.db import models
from core.models import BaseModel


class AnonymousUserPaymentInfo(BaseModel):
    id = models.AutoField(primary_key=True)
    anonymous_user = models.ForeignKey('anonymous_users.AnonymousUser', related_name='payment_info')
    card = models.ForeignKey('cards.Card', related_name='anonymous_user_payment_info')
    stripe_token = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'anonymous_users'
        db_table = 'anonymous_user_payment_info'
        verbose_name = 'Anonymous User Payment Info'
        verbose_name_plural = 'Anonymous User Payment Info'
