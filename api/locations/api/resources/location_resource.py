# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from locations.models import Location

class LocationResource(ModelResource):
    class Meta:
        resource_name = 'locations'
        queryset = Location.objects.all()
        allowed_methods = ['get']
