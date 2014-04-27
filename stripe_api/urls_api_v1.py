from django.conf.urls import patterns, url

from api import ChargeProcess, ChargeRetrieve, CardList


urlpatterns = patterns('',
    # Card Processing
    url(r'^charges/process/$', ChargeProcess.as_view(), name="api-v1-charge-process"),

    # Card Retrieve
    url(r'^charges/retrieve/(?P<id>[a-z0-9\-]+)/$', ChargeRetrieve.as_view(), name="api-v1-charge-retrieve"),

    # Card Create
    url(r'^users/(?P<user_id>[0-9]+)/cards/$', CardList.as_view(), name="api-v1-user-cards-list"),
)
