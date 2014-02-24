from django.shortcuts import render

def index(request):
    context = {
        'welcome_text': 'Welcome to DinDin!'
    }

    return render(request, 'core/index.html', context)