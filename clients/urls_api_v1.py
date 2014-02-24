# Django
from django.conf.urls import patterns, url, include

# Local Apps
from clients.api.resources import ClientDetail, ClientLocationList, ClientLocationDetail, ClientLocationDetailDetail

urlpatterns = patterns('',
    # Clients
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name="api-v1-client-detail"),

    # Client Locations
    url(r'^clients/(?P<client_id>[0-9]+)/locations/$', ClientLocationList.as_view(), name="api-v1-client-location-list"),
    url(r'^clients/(?P<client_id>[0-9]+)/locations/(?P<pk>[0-9]+)/$', ClientLocationDetail.as_view(), name="api-v1-client-location-detail"),


    # Client Location Detail
    url(r'^clients/(?P<client_id>[0-9]+)/locations/(?P<client_location_id>[0-9]+)/details/$', ClientLocationDetailDetail.as_view(), name="api-v1-client-location-detail-detail"),

    # # Package Permissions
    # url(r'^packages/(?P<package_id>[0-9]+)/permissions/$', api.PermissionList.as_view(), name="api-v2-package-permissions-list"),

    # # Package Plans
    # url(r'^packages/(?P<package_id>[0-9]+)/plans/$', api.PlanList.as_view(), name="api-v2-package-plan-list"),
    # url(r'^packages/(?P<package_id>[0-9]+)/plans/(?P<pk>[0-9]+)/$', api.PlanDetail.as_view(), name="api-v2-package-plan-detail"),
)
