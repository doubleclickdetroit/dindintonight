# Django
from django.conf.urls import patterns, url, include

# Django Rest Framework
from rest_framework import routers

# 3rd party
from drops import viewsets

router = routers.DefaultRouter()
router.register(r'drops', viewsets.DropViewSet)
router.register(r'drop-meals', viewsets.DropMealViewSet)

# Wire up our API using automatic URL routing from Django Rest Framework ;-)
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
