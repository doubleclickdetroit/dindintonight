from django.http import Http404
from django.shortcuts import render

from clients.api import ClientLocationSearchList
from franchises.models import Franchise


def index(request, slug):
    try:
        franchise = Franchise.objects.get(slug=slug)
    except Franchise.DoesNotExist:
        raise Http404

    client_location_search_list = ClientLocationSearchList().internal_request(request, franchise_id=franchise.pk)

    context = {
        'franchise': franchise,
        'client_locations': client_location_search_list
    }

    return render(request, 'franchises/index.html', context)