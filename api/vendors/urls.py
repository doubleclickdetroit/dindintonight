# Django
from django.conf.urls import patterns, include

# TastyPie
from tastypie.api import Api

# Local Apps
from vendors.api.resources import VendorResource, VendorLocationResource

v1_api = Api(api_name='v1')
v1_api.register(VendorResource())
v1_api.register(VendorLocationResource())

urlpatterns = patterns('',
  (r'^api/', include(v1_api.urls)),
)
