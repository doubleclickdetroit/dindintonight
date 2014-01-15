from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import locations.urls as location_urls
import drops.urls as drop_urls
import meals.urls as meal_urls
import persons.urls as person_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # All Auth
    url(r'^accounts/', include('allauth.urls')),

    # Location Module URLs
    url(r'^api/', include(location_urls)),

    # Drop Module URLs
    url(r'^api/', include(drop_urls)),

    # Meal Module URLs
    url(r'^api/', include(meal_urls)),

    # Person Module URLs
    url(r'^api/', include(person_urls)),

    # Browseable Rest Framework Urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
