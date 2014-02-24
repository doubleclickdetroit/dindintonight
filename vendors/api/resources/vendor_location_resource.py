# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from vendors.models import VendorLocation
# from vendors.api.resources import VendorResource
# from locations.api.resources import LocationResource

class VendorLocationResource(ModelResource):
    # vendor = fields.ToOneField(VendorResource, 'vendor')
    # location = fields.ToOneField(LocationResource, 'location', full=True)
    # meals = fields.ToManyField('meals.api.resources.MealResource', 'meals', related_name='vendor_location', full=True, null=True, blank=True)

    class Meta:
        resource_name = 'vendor-locations'
        queryset = VendorLocation.objects.all()
        allowed_methods = ['get']
