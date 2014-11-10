import logging

from rest_framework.viewsets import GenericViewSet
from rest_framework import generics

from .models import Page
from .serializers import PageSerializer

LOG = logging.getLogger(__name__)


class PageAPIView(generics.ListAPIView,
                  generics.RetrieveAPIView,
                  GenericViewSet):
    """
    Page API view
    """
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    lookup_fields = ('id', 'url')
