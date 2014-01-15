# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import Drop
from .models import DropMeal

class DropAdmin(BaseModelAdmin):
    list_display = ['id', 'location', 'date_and_time', 'timezone', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(Drop, DropAdmin)

class DropMealAdmin(BaseModelAdmin):
    list_display = ['id', 'drop', 'meal', 'quantity', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(DropMeal, DropMealAdmin)
