# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from users.models import User
from cards.models import Card

class UserPaymentInfo(BaseModel):
    id              = models.IntegerField(primary_key=True)
    user            = models.ForeignKey(User, related_name='payment_info')
    card            = models.ForeignKey(Card, related_name='user_payment_info')
    stripe_token    = models.CharField(max_length=45)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'users'
        db_table = 'user_payment_info'
        verbose_name = 'User Payment Info'
        verbose_name_plural = 'User Payment Info'
