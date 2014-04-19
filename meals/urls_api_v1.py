# Django
from django.conf.urls import patterns, url, include

# Local Apps
from meals.api import MealList, MealDetail

urlpatterns = patterns('',
    # Locations
    url(r'^vendors/(?P<vendor_id>[0-9]+)/locations/(?P<vendor_location_id>[0-9]+)/meals/$', MealList.as_view(),
        name="api-v1-meal-list"),
    url(r'^vendors/(?P<vendor_id>[0-9]+)/locations/(?P<vendor_location_id>[0-9]+)/meals/(?P<pk>[0-9]+)/$',
        MealDetail.as_view(), name="api-v1-meal-detail"),
)
