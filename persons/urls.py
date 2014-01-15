# Django
from django.conf.urls import patterns, url, include

# Django Rest Framework
from rest_framework import routers

# 3rd party
from persons import viewsets

router = routers.DefaultRouter()
router.register(r'persons', viewsets.PersonViewSet)
router.register(r'person-addresses', viewsets.PersonAddressViewSet)

# Wire up our API using automatic URL routing from Django Rest Framework ;-)
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
