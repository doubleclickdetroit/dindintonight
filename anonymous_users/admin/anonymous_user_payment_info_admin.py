from django.contrib import admin
from core.admin import BaseModelAdmin
from anonymous_users.models import AnonymousUserPaymentInfo


class AnonymousUserPaymentInfoAdmin(BaseModelAdmin):
    list_display = ['id', 'anonymous_user', 'card', 'stripe_token', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(AnonymousUserPaymentInfo, AnonymousUserPaymentInfoAdmin)
