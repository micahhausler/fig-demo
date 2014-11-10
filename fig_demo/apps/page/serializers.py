import logging

from django.conf import settings
from rest_framework import serializers
from .models import Page

LOG = logging.getLogger(__name__)


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page

    called_time = serializers.DateTimeField(format=settings.DATE_FORMAT_STRING)
