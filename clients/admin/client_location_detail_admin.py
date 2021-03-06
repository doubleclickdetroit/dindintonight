from django.contrib import admin

from core.admin import BaseModelAdmin
from clients.models import ClientLocationDetail


class ClientLocationDetailAdmin(BaseModelAdmin):
    list_display = ['id', 'client_location', 'address1', 'address2', 'address3', 'latitude', 'phone_number',
                    'manager_name', 'longitude', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(ClientLocationDetail, ClientLocationDetailAdmin)
