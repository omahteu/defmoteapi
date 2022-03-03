from rest_framework import viewsets
from quartos.models import Quarto
from quartos.serializer import QuartoSerializer


class QuartoViewSet(viewsets.ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer
