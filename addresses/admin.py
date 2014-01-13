# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import Address

class AddressAdmin(BaseModelAdmin):
    list_display = ['id', 'location', 'address', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(Address, AddressAdmin)
