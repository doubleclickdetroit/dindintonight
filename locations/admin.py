# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import Location
from .models import LocationMeal

class LocationAdmin(BaseModelAdmin):
    list_display = ['id', 'name', 'address', 'city', 'state', 'zip', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(Location, LocationAdmin)

class LocationMealAdmin(BaseModelAdmin):
    list_display = ['id', 'location', 'meal', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(LocationMeal, LocationMealAdmin)
