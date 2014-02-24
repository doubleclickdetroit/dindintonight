# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from anonymous_users.models import AnonymousUser

class AnonymousUserAdmin(BaseModelAdmin):
    list_display = ['id', 'location', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(AnonymousUser, AnonymousUserAdmin)
