from django.contrib import admin
from core.admin import BaseModelAdmin
from users.models import UserStripeCard


class UserStripeCardAdmin(BaseModelAdmin):
    list_display = ['id', 'user', 'card_id', 'name', 'description', 'last4', 'type', 'expiration_month',
                    'expiration_year', 'fingerprint', 'country', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(UserStripeCard, UserStripeCardAdmin)
