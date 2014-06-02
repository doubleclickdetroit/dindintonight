from django.http import Http404
from django.shortcuts import render
from franchises.models import Franchise


def index(request, slug):
    try:
        franchise = Franchise.objects.get(slug=slug)
    except Franchise.DoesNotExist:
        raise Http404

    context = {
        'franchise': franchise
    }

    return render(request, 'franchises/index.html', context)