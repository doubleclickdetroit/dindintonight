from django.db import models
from django.db.models.signals import post_save

from core.models import BaseModel


class ClientLocationMeal(BaseModel):
    id = models.AutoField(primary_key=True)
    client_location = models.ForeignKey('clients.ClientLocation', related_name='meals')
    meal = models.ForeignKey('meals.Meal', related_name='clients')
    is_enabled = models.BooleanField(default=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clients'
        db_table = 'client_location_meals'
        verbose_name = 'Client Location Meal'
        verbose_name_plural = 'Client Location Meals'

    def __unicode__(self):
        return '{0} - {1} - {2} - {3}'.format(self.pk, self.client_location.client.name,
                                              self.client_location.location.zip_code, self.meal.name)


def client_location_meal_post_save_handler(sender, instance, **kwargs):
    from clients.api import ClientLocationMealList, ClientLocationSearchList

    # bust the cache on the ClientLocationMealList
    client_location_meal_list = ClientLocationMealList()
    client_location_meal_list.bust_cache()

    # bust the cache on the ClientLocationSearchList
    client_location_search_list = ClientLocationSearchList()
    client_location_search_list.bust_cache()

post_save.connect(client_location_meal_post_save_handler, sender=ClientLocationMeal)
