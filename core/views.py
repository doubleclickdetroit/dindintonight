from django.shortcuts import render

from persons.models import Person


def index(request):
    return render(request, 'core/index.html', context)