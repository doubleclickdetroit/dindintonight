# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import DropMeal

class DropMealAdmin(BaseModelAdmin):
    list_display = ['id', 'drop', 'meal', 'quantity', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(DropMeal, DropMealAdmin)
