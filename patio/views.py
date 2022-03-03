from rest_framework import viewsets
from patio.models import Patio
from patio.serializer import PatioSerializer


class PatioViewSet(viewsets.ModelViewSet):
    queryset = Patio.objects.all()
    serializer_class = PatioSerializer
