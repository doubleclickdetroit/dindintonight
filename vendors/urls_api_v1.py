# Django
from django.conf.urls import patterns, url, include

# Local Apps
from vendors.api import VendorDetail, VendorList, VendorLocationList, VendorLocationDetail, VendorUserDetail, \
    VendorUserList

urlpatterns = patterns('',
    # Vendors
    url(r'^vendors/(?P<pk>[0-9]+)/$', VendorDetail.as_view(), name="api-v1-vendor-detail"),
    url(r'^vendors/$', VendorList.as_view(), name="api-v1-vendor-list"),

    # Vendor Locations
    url(r'^vendors/(?P<vendor_id>[0-9]+)/locations/$', VendorLocationList.as_view(),
        name="api-v1-vendor-location-list"),
    url(r'^vendors/(?P<vendor_id>[0-9]+)/locations/(?P<pk>[0-9]+)/$', VendorLocationDetail.as_view(),
        name="api-v1-vendor-location-detail"),

    # Vendor Users
    url(r'^vendors/(?P<vendor_id>[0-9]+)/users/$', VendorUserList.as_view(),
        name="api-v1-vendor-user-list"),
    url(r'^vendors/(?P<vendor_id>[0-9]+)/users/(?P<pk>[0-9]+)/$', VendorUserDetail.as_view(),
        name="api-v1-vendor-user-detail"),
)
