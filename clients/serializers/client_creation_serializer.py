# Core
import re

# Django
from django.core import validators
from django.utils.translation import ugettext_lazy as _

# Django Rest Framework
from rest_framework import serializers

class ClientCreationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, min_length=1,
                                     validators=[
                                         validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                   _('Enter a valid username.'), 'invalid')
                                     ])
    first_name = serializers.CharField(max_length=30, min_length=1)
    last_name = serializers.CharField(max_length=30, min_length=1)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, min_length=6)
