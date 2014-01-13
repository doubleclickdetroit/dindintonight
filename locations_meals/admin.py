# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import LocationMeal

class LocationMealAdmin(BaseModelAdmin):
    list_display = ['id', 'location', 'meal', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(LocationMeal, LocationMealAdmin)
