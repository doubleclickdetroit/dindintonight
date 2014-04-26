from django.conf.urls import patterns, url

from charges.api import ProcessCharge


urlpatterns = patterns('',
    # Processing
    url(r'^charges/process/$', ProcessCharge.as_view(), name="api-v1-charge-process"),
)
