# Django
from django.db import models

# Local Apps
from core.utils import debug_print
from core.models import BaseModel
from users.models import User
from meals.models import Meal


class UserMealPurchaseHistory(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user_meal_purchase_history')
    meal = models.ForeignKey(Meal, related_name='user_meal_purchase_history')
    purchased_on = models.DateTimeField()
    deliver_on = models.DateTimeField()
    delivered_on = models.DateTimeField(blank=True, null=True)
    cancelled_on = models.DateTimeField(blank=True, null=True)
    is_delivered = models.BooleanField(default=False, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'users'
        db_table = 'user_meal_purchase_history'
        verbose_name = 'User Meal Purchase History'
        verbose_name_plural = 'User Meal Purchase History'
