from django.shortcuts import render

from persons.models import Person


def index(request):
    context = {
        'welcome_text': 'Welcome to DinDin!'
    }

    return render(request, 'core/index.html', context)