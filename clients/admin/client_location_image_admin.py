from django.contrib import admin
from core.admin import BaseModelAdmin
from clients.models import ClientLocationImage


class ClientLocationImageAdmin(BaseModelAdmin):
    list_display = ['id', 'client_location', 'name', 'description', 'location', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(ClientLocationImage, ClientLocationImageAdmin)