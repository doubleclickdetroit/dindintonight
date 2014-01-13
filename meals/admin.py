# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import Meal


class MealAdmin(BaseModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'price', 'created', 'modified']
    readonly_fields = ['created', 'modified']

admin.site.register(Meal, MealAdmin)
