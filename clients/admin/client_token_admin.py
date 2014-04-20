from django.contrib import admin
from core.admin import BaseModelAdmin
from clients.models import ClientToken


class ClientTokenAdmin(BaseModelAdmin):
    list_display = ['id', 'client', 'value', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(ClientToken, ClientTokenAdmin)
