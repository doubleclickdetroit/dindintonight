from django.contrib import admin
from core.admin import BaseModelAdmin
from vendors.models import VendorUser


class VendorUserAdmin(BaseModelAdmin):
    list_display = ['id', 'vendor', 'user', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(VendorUser, VendorUserAdmin)
