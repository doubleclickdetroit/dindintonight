import re


def show_django_debug_toolbar(request):
    uri = request.get_full_path()

    if re.match(r'/api/', uri):
        return True

    return False