from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # # Home
    url(r'^$', views.index, name='index'),
    # # url(r'^$', TemplateView.as_view(template_name='base.html')),

    # All Auth
    url(r'^accounts/', include('allauth.urls')),

    # Browseable Rest Framework Urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # API
    url(r'^api/v1/', include('franchises.urls_api_v1')),
    url(r'^api/v1/', include('locations.urls_api_v1')),
    url(r'^api/v1/', include('clients.urls_api_v1')),
    url(r'^api/v1/', include('vendors.urls_api_v1')),
    url(r'^api/v1/', include('meals.urls_api_v1')),
    url(r'^api/v1/', include('users.urls_api_v1')),
)
