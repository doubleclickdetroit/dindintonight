from django.contrib import admin
from core.admin import BaseModelAdmin
from anonymous_users.models import AnonymousUserMealPurchaseHistory

class AnonymousUserMealPurchaseHistoryAdmin(BaseModelAdmin):
    list_display = ['id', 'anonymous_user', 'meal', 'purchased_on', 'delivered_on', 'cancelled_on', 'is_delivered',
                    'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(AnonymousUserMealPurchaseHistory, AnonymousUserMealPurchaseHistoryAdmin)
