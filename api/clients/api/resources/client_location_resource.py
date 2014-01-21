# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from clients.models import ClientLocation
from locations.api.resources import LocationResource

class ClientLocationResource(ModelResource):
    # meals = fields.ToOneField('clients.api.resources.ClientLocationMealResource', 'meals', full=True)
    # detail = fields.ToOneField('clients.api.resources.ClientLocationDetailResource', 'detail', full=True)
    # location = fields.ToOneField(LocationResource, 'location', full=True)
    client = fields.ToOneField('clients.api.resources.ClientResource', 'client')

    class Meta:
        resource_name = 'client-locations'
        queryset = ClientLocation.objects.all()
        allowed_methods = ['get']
