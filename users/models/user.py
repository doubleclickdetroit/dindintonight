from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.renderers import JSONRenderer
from core.models import BaseModel
import stripe
from leads.models import Lead


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

    @property
    def serialized(self):
        from users.serializers import UserSerializer
        return UserSerializer(self).data

    @property
    def json(self):
        from users.serializers import UserSerializer
        return JSONRenderer().render(UserSerializer(self).data)


def user_post_save_handler(sender, instance, **kwargs):
    created = kwargs.get('created')

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if created:
        stripe_customer = stripe.Customer.create(
            email=instance.email,
            description='{0} - {1}'.format(instance.username, instance.get_full_name())
        )

        from users.models import UserStripeCustomer
        customer = UserStripeCustomer()
        customer.user = instance
        customer.customer_id = stripe_customer.id
        customer.save()

        # Clean up any leads that we had due to them now being a user of the site
        Lead.objects.filter(email=instance.email).delete()


    else:
        stripe_customer = stripe.Customer.retrieve(instance.customer.customer_id)
        stripe_customer.email = instance.email
        stripe_customer.description = '{0} - {1}'.format(instance.username, instance.get_full_name())
        stripe_customer.save()

    from users.api import UserList
    # bust the cache on the UserList
    user_list = UserList()
    user_list.bust_cache()

post_save.connect(user_post_save_handler, sender=User)
