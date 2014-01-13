# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import PersonAddress

class PersonAddressAdmin(BaseModelAdmin):
    list_display = ['id', 'person', 'address', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(PersonAddress, PersonAddressAdmin)
