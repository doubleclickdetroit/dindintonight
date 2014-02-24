# Django
from django.conf.urls import patterns, url, include

# Local Apps
from vendors.api.resources import VendorDetail, VendorLocationList, VendorLocationDetail

urlpatterns = patterns('',
    # Vendors
    url(r'^vendors/(?P<pk>[0-9]+)/$', VendorDetail.as_view(), name="api-v1-vendor-detail"),

    # Vendor Locations
    url(r'^vendors/(?P<vendor_id>[0-9]+)/locations/$', VendorLocationList.as_view(), name="api-v1-vendor-location-list"),
    url(r'^vendors/(?P<vendor_id>[0-9]+)/locations/(?P<pk>[0-9]+)/$', VendorLocationDetail.as_view(), name="api-v1-vendor-location-detail"),
)
