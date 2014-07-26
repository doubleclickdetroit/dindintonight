from django.contrib import admin

from core.admin import BaseModelAdmin
from clients.models import ClientLocation


class ClientLocationAdmin(BaseModelAdmin):
    list_display = ['id', 'client', 'location', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(ClientLocation, ClientLocationAdmin)
