from django.contrib import admin
from core.admin import BaseModelAdmin
from locations.models import Location


class LocationAdmin(BaseModelAdmin):
    list_display = ['id', 'city', 'state', 'zip_code', 'latitude', 'longitude', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Location, LocationAdmin)
