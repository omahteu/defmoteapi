from rest_framework import viewsets
from comanda.models import Comanda
from comanda.serializer import ComandaSerializer


class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer
