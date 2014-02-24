# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from users.models import UserMealPurchaseHistory

class UserMealPurchaseHistoryAdmin(BaseModelAdmin):
    list_display = ['id', 'user', 'meal', 'purchased_on', 'deliver_on', 'delivered_on', 'cancelled_on', 'is_delivered', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(UserMealPurchaseHistory, UserMealPurchaseHistoryAdmin)
