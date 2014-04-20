from django.contrib import admin
from core.admin import BaseModelAdmin
from vendors.models import VendorLocation


class VendorLocationAdmin(BaseModelAdmin):
    list_display = ['id', 'vendor', 'location', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(VendorLocation, VendorLocationAdmin)
