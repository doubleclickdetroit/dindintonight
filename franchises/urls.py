from django.conf.urls import patterns, url
from franchises import views


urlpatterns = patterns('',
    url(r'^(?P<slug>[a-z0-9\-]+)/$', views.index, name='franchise-index'),
)
