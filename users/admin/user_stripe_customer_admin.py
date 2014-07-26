from django.contrib import admin

from core.admin import BaseModelAdmin
from users.models import UserStripeCustomer


class UserStripeCustomerAdmin(BaseModelAdmin):
    list_display = ['id', 'user', 'customer_id', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(UserStripeCustomer, UserStripeCustomerAdmin)
