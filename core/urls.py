from django.conf.urls import patterns, include, url
from django.contrib import admin

import views


admin.autodiscover()

urlpatterns = patterns('',
    # Home
    url(r'^$', views.index, name='index'),
    # url(r'^$', TemplateView.as_view(template_name='base.html')),

    # All Auth
    url(r'^accounts/', include('allauth.urls')),

    # Browseable Rest Framework Urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Franchises
    url(r'^franchises/', include('franchises.urls')),

    # API
    url(r'^api/v1/', include('stripe_api.urls_api_v1')),
    url(r'^api/v1/', include('franchises.urls_api_v1')),
    url(r'^api/v1/', include('locations.urls_api_v1')),
    url(r'^api/v1/', include('clients.urls_api_v1')),
    url(r'^api/v1/', include('vendors.urls_api_v1')),
    url(r'^api/v1/', include('meals.urls_api_v1')),
    url(r'^api/v1/', include('users.urls_api_v1')),
    url(r'^api/v1/', include('leads.urls_api_v1')),
)
