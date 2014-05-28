from django.contrib import admin
from core.admin import BaseModelAdmin
from leads.models import Lead


class LeadAdmin(BaseModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'created', 'modified']
    readonly_fields = ['id', 'franchise', 'created', 'modified']


admin.site.register(Lead, LeadAdmin)
