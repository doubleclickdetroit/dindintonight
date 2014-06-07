from django.contrib import admin
from core.admin import BaseModelAdmin
from meals.models import MealImage


class MealImageAdmin(BaseModelAdmin):
    list_display = ['id', 'meal', 'name', 'description', 'location', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(MealImage, MealImageAdmin)
