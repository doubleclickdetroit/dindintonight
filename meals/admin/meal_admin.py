from django.contrib import admin

from core.admin import BaseModelAdmin
from meals.models import Meal


class MealAdmin(BaseModelAdmin):
    list_display = ['id', 'vendor_location', 'name', 'description', 'price', 'available_starting', 'available_ending',
                    'is_deleted', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Meal, MealAdmin)
