from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import views

# import anonymous_users.urls as anonymous_users_urls
# import cards.urls           as cards_urls
# import clients.urls         as clients_urls
# import locations.urls       as locations_urls
# import meals.urls           as meals_urls
# import users.urls           as users_urls
# import vendors.urls         as vendors_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # # Home
    # url(r'^$', views.index, name='index'),
    # # url(r'^$', TemplateView.as_view(template_name='base.html')),

    # All Auth
    url(r'^accounts/', include('allauth.urls')),

    # # Anonymous Users Module URLs
    # url(r'^', include(anonymous_users_urls)),

    # # Cards Module URLs
    # url(r'^', include(cards_urls)),

    # # Clients Module URLs
    # url(r'^', include(clients_urls)),

    # Locations Module URLs
    # url(r'^', include(locations_urls)),

    # # Meals Module URLs
    # url(r'^', include(meals_urls)),

    # # Users Module URLs
    # url(r'^', include(user_urls)),

    # Vendors Module URLs
    # url(r'^', include(vendors_urls)),

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
    url(r'^api/v1/', include('locations.urls_api_v1')),
    url(r'^api/v1/', include('clients.urls_api_v1')),
    url(r'^api/v1/', include('vendors.urls_api_v1')),
)
