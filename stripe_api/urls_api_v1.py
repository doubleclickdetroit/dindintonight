from django.conf.urls import patterns, url

from api import ChargeProcess, ChargeRetrieve, UserCardList, UserCardDetail


urlpatterns = patterns('',
    # Charge Processing
    url(r'^charges/process/$', ChargeProcess.as_view(), name="api-v1-charge-process"),

    # Charge Retrieve
    url(r'^charges/retrieve/(?P<id>[a-z0-9\-]+)/$', ChargeRetrieve.as_view(), name="api-v1-charge-retrieve"),

    # Cards
    url(r'^users/(?P<user_id>[0-9]+)/cards/$', UserCardList.as_view(), name="api-v1-user-cards-list"),
    url(r'^users/(?P<user_id>[0-9]+)/cards/(?P<pk>[0-9]+)/$', UserCardDetail.as_view(), name="api-v1-user-cards-detail"),
)
