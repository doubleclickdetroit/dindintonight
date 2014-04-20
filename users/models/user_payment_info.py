from django.db import models
from core.models import BaseModel


class UserPaymentInfo(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', related_name='payment_info')
    card = models.ForeignKey('cards.Card', related_name='user_payment_info')
    stripe_token = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'users'
        db_table = 'user_payment_info'
        verbose_name = 'User Payment Info'
        verbose_name_plural = 'User Payment Info'
