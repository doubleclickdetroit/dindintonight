# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# 3rd party
# from model_utils import FieldTracker

from core.utils import debug_print
from core.models import BaseModel


class Person(AbstractUser, BaseModel):
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'persons'
        db_table = 'persons'
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
