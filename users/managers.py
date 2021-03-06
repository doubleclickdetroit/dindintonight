from django.contrib.auth.models import UserManager
from django.contrib.auth import get_user_model

from core.managers import NoCountManager


class UserManager(UserManager, NoCountManager):
    '''
    Custom manager to implement our custom create_user
    and create_superuser methods.
    '''

    def create_user(self, username, password=None, **extra_fields):
        '''
        Creates and saves a Person with the given username.
        '''
        if not username:
            raise ValueError('A valid username is required.')

        person =  get_user_model()(username=username, **extra_fields)
        if password is not None:
            person.set_password(password)

        # The person has not logged in
        person.last_login = None
        person.save(using=self._db)
        return person

    def create_superuser(self, username, password, **extra_fields):
        '''
        Creates and saves a superuser Person.
        '''
        if password is None:
            raise Exception("Must supply a password for new superusers.")

        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
