from django.conf.urls import patterns, url
from franchises.api import FranchiseList, FranchiseDetail

urlpatterns = patterns('',
    # Franchises
    url(r'^franchises/$', FranchiseList.as_view(), name="api-v1-franchise-list"),
    url(r'^franchises/(?P<pk>[0-9]+)/$', FranchiseDetail.as_view(), name="api-v1-franchise-detail"),
)
