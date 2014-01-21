# Django
from django.conf.urls import patterns, include

# TastyPie
from tastypie.api import Api

# Local Apps
from clients.api.resources import ClientLocationDetailResource, ClientLocationMealResource, ClientLocationResource, ClientResource

v1_api = Api(api_name='v1')
v1_api.register(ClientLocationDetailResource())
v1_api.register(ClientLocationMealResource())
v1_api.register(ClientLocationResource())
v1_api.register(ClientResource())

urlpatterns = patterns('',
  (r'^api/', include(v1_api.urls)),
)
