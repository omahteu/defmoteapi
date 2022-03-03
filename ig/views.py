from rest_framework import viewsets
from ig.models import Ig
from ig.serializer import IgSerializer


class IgViewSets(viewsets.ModelViewSet):
    queryset = Ig.objects.all()
    serializer_class = IgSerializer
