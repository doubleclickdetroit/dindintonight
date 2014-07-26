from django.contrib import admin

from core.admin import BaseModelAdmin
from clients.models import Client


class ClientAdmin(BaseModelAdmin):
    list_display = ['id', 'name', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Client, ClientAdmin)
