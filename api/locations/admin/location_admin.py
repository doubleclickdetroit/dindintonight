# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from locations.models import Location

class LocationAdmin(BaseModelAdmin):
    list_display = ['id', 'city', 'state', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Location, LocationAdmin)
