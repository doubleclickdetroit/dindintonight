from django.db import models
from core.models import BaseModel


class UserStripeCustomer(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField('users.User', related_name='customer')
    customer_id = models.CharField(db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'customers'
        db_table = 'user_stripe_customers'
        verbose_name = 'User Stripe Customers'
        verbose_name_plural = 'User Stripe Customers'
