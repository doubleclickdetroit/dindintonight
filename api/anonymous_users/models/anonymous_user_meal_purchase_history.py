# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from anonymous_users.models import AnonymousUser
from meals.models import Meal

class AnonymousUserMealPurchaseHistory(BaseModel):
    id              = models.IntegerField(primary_key=True)
    anonymous_user  = models.ForeignKey(AnonymousUser, related_name='meal_purchase_history')
    meal            = models.ForeignKey(Meal, related_name='anonymous_user_purchase_history')
    purchased_on    = models.DateTimeField()
    deliver_on      = models.DateTimeField()
    delivered_on    = models.DateTimeField(blank=True, null=True)
    cancelled_on    = models.DateTimeField(blank=True, null=True)
    is_delivered    = models.IntegerField()
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'anonymous_users'
        db_table = 'anonymous_user_meal_purchase_history'
        verbose_name = 'Anonymous User Meal Purchase History'
        verbose_name_plural = 'Anonymous User Meal Purchase History'
