# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from clients.models import Client

class ClientResource(ModelResource):
    locations = fields.ToManyField('clients.api.resources.ClientLocationResource', 'locations', related_name='client', full=True, null=True, blank=True)

    class Meta:
        resource_name = 'clients'
        queryset = Client.objects.all()
        allowed_methods = ['get']
