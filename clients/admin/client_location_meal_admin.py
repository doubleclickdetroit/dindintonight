# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from clients.models import ClientLocationMeal

class ClientLocationMealAdmin(BaseModelAdmin):
    list_display = ['id', 'client_location', 'meal', 'is_enabled', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(ClientLocationMeal, ClientLocationMealAdmin)
