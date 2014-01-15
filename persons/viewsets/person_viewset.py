# Django Rest Framework
from rest_framework import viewsets

# 3rd party
from persons.models import Person
from persons.serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
