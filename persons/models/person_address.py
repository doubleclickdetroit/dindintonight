# Django
from django.db import models

# 3rd party
from core.models import BaseModel
from addresses.models import Address
from .person import Person

class PersonAddress(BaseModel):
    id              = models.AutoField(primary_key=True)
    person          = models.ForeignKey(Person)
    address         = models.ForeignKey(Address)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'persons'
        db_table = 'person_addresses'
        verbose_name = 'Person Address'
        verbose_name_plural = 'Person Addresses'
