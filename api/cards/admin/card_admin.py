# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from cards.models import Card

class CardAdmin(BaseModelAdmin):
    list_display = ['id', 'name', 'created', 'modified']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Card, CardAdmin)
