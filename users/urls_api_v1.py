from django.conf.urls import patterns, url
from users.api import UserDetail, UserList, UserLocationList #, UserLocationDetail

urlpatterns = patterns('',
    # Users
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name="api-v1-user-detail"),
    url(r'^users/$', UserList.as_view(), name="api-v1-user-list"),

    # User Locations
    url(r'^users/(?P<user_id>[0-9]+)/locations/$', UserLocationList.as_view(), name="api-v1-user-location-list"),
    # url(r'^users/(?P<user_id>[0-9]+)/locations/(?P<pk>[0-9]+)/$', UserLocationDetail.as_view(),
    #     name="api-v1-user-location-detail"),
)
