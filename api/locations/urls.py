# Django
from django.conf.urls import patterns, include

# TastyPie
from tastypie.api import Api

# Local Apps
from locations.api.resources import LocationResource

v1_api = Api(api_name='v1')
v1_api.register(LocationResource())

urlpatterns = patterns('',
  (r'^api/', include(v1_api.urls)),
)
