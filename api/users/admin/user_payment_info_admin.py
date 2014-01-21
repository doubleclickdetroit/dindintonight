# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from users.models import UserPaymentInfo

class UserPaymentInfoAdmin(BaseModelAdmin):
    list_display = ['id', 'user', 'card', 'stripe_token', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(UserPaymentInfo, UserPaymentInfoAdmin)
