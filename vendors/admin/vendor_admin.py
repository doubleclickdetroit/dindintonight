from django.contrib import admin
from core.admin import BaseModelAdmin
from vendors.models import Vendor


class VendorAdmin(BaseModelAdmin):
    list_display = ['id', 'name', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Vendor, VendorAdmin)
