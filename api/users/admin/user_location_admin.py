# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from users.models import UserLocation

class UserLocationAdmin(BaseModelAdmin):
    list_display = ['id', 'user', 'location', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(UserLocation, UserLocationAdmin)
