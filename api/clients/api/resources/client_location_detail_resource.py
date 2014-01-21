# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from clients.models import ClientLocationDetail

class ClientLocationDetailResource(ModelResource):
    class Meta:
        resource_name = 'client-location-details'
        queryset = ClientLocationDetail.objects.all()
        allowed_methods = ['get']
