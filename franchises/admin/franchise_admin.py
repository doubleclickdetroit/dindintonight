from django.contrib import admin
from core.admin import BaseModelAdmin
from franchises.models import Franchise


class FranchiseAdmin(BaseModelAdmin):
    list_display = ['id', 'owner', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Franchise, FranchiseAdmin)
