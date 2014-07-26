from django.contrib import admin

from core.admin import BaseModelAdmin
from clients.models import ClientHost


class ClientHostAdmin(BaseModelAdmin):
    list_display = ['id', 'client', 'value', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(ClientHost, ClientHostAdmin)
