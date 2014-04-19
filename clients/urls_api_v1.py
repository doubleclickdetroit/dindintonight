# Django
from django.conf.urls import patterns, url, include

# Local Apps
from clients.api import ClientList, ClientDetail, ClientLocationList, ClientLocationDetail, ClientLocationDetailDetail

urlpatterns = patterns('',
    # Clients
    url(r'^clients/$', ClientList.as_view(), name="api-v1-client-list"),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name="api-v1-client-detail"),

    # Client Locations
    url(r'^clients/(?P<client_id>[0-9]+)/locations/$', ClientLocationList.as_view(),
        name="api-v1-client-location-list"),
    url(r'^clients/(?P<client_id>[0-9]+)/locations/(?P<pk>[0-9]+)/$', ClientLocationDetail.as_view(),
        name="api-v1-client-location-detail"),


    # Client Location Detail
    url(r'^clients/(?P<client_id>[0-9]+)/locations/(?P<client_location_id>[0-9]+)/details/$',
        ClientLocationDetailDetail.as_view(), name="api-v1-client-location-detail-detail"),
)
