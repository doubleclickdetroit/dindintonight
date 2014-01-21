# TastyPie
from tastypie import fields
from tastypie.resources import ModelResource

# Local Apps
from vendors.models import Vendor

class VendorResource(ModelResource):
    locations = fields.ToManyField('vendors.api.resources.VendorLocationResource', 'locations', related_name='vendor', full=True, null=True, blank=True)

    class Meta:
        resource_name = 'vendors'
        queryset = Vendor.objects.all()
        allowed_methods = ['get']
