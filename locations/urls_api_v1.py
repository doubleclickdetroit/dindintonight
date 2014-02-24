# Django
from django.conf.urls import patterns, url, include

# Local Apps
from locations.api.resources import LocationList, LocationDetail

urlpatterns = patterns('',
    # Locations
    url(r'^locations/$', LocationList.as_view(), name="api-v1-location-list"),
    url(r'^locations/(?P<pk>[0-9]+)/$', LocationDetail.as_view(), name="api-v1-location-detail"),

    # # Package Permissions
    # url(r'^packages/(?P<package_id>[0-9]+)/permissions/$', api.PermissionList.as_view(), name="api-v2-package-permissions-list"),

    # # Package Plans
    # url(r'^packages/(?P<package_id>[0-9]+)/plans/$', api.PlanList.as_view(), name="api-v2-package-plan-list"),
    # url(r'^packages/(?P<package_id>[0-9]+)/plans/(?P<pk>[0-9]+)/$', api.PlanDetail.as_view(), name="api-v2-package-plan-detail"),
)
