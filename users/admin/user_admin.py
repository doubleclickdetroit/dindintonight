# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from users.models import User

class UserAdmin(BaseModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active', 'date_joined',
                    'created', 'modified']
    # fieldsets = (
    #     ('Basic', {
    #         'fields': ('id', 'username', 'email',)
    #     }),
    #     ('Permissions', {
    #         'fields': ('is_active', 'is_staff', 'is_superuser',)
    #     }),
    #     ('Chronology', {
    #         'fields': ('last_login', 'created', 'modified')
    #     })
    # )
    readonly_fields = ['id', 'last_login', 'date_joined', 'created', 'modified']


admin.site.register(User, UserAdmin)
