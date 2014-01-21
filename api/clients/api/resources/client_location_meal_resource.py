# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from clients.models import ClientLocationMeal

class ClientLocationMealResource(ModelResource):
    class Meta:
        resource_name = 'client-location-meals'
        queryset = ClientLocationMeal.objects.all()
        allowed_methods = ['get']
