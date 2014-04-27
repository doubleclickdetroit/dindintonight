from django.conf.urls import patterns, url

from api import ChargeProcess, ChargeRetrieve


urlpatterns = patterns('',
    # Processing
    url(r'^charges/process/$', ChargeProcess.as_view(), name="api-v1-charge-process"),

    # Retrieve
    url(r'^charges/retrieve/(?P<id>[a-z0-9\-]+)/$', ChargeRetrieve.as_view(), name="api-v1-charge-retrieve"),
)
