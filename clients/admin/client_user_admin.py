# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from clients.models import ClientUser

class ClientUserAdmin(BaseModelAdmin):
    list_display = ['id', 'client', 'user', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(ClientUser, ClientUserAdmin)
