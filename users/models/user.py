from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from core.models import BaseModel


class User(AbstractUser, BaseModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'users'
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


def user_post_save_handler(sender, instance, **kwargs):
    from users.api import UserList

    # bust the cache on the UserList
    user_list = UserList()
    user_list.bust_cache()

post_save.connect(user_post_save_handler, sender=User)
