from django.conf.urls import patterns, url
from users.api import UserDetail, UserList

urlpatterns = patterns('',
    # Users
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name="api-v1-user-detail"),
    url(r'^users/$', UserList.as_view(), name="api-v1-user-list"),
)
