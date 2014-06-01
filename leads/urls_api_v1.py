from django.conf.urls import patterns, url
from leads.api import LeadList

urlpatterns = patterns('',
    # Leads
    url(r'^franchises/(?P<franchise_id>\d+)/leads/$', LeadList.as_view(), name="api-v1-lead-list"),
    # url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name="api-v1-client-detail"),
)
