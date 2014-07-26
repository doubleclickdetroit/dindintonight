from django.conf.urls import patterns, url

from locations.api import LocationList, LocationDetail


urlpatterns = patterns('',
    # Locations
    url(r'^locations/$', LocationList.as_view(), name="api-v1-location-list"),
    url(r'^locations/(?P<pk>[0-9]+)/$', LocationDetail.as_view(), name="api-v1-location-detail"),
)
