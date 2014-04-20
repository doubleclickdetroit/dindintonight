from django.conf.urls import patterns, url, include
from rest_framework import routers
from users import viewsets

router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)

# Wire up our API using automatic URL routing from Django Rest Framework ;-)
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
