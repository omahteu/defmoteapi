from rest_framework import viewsets
from caixa.models import Caixa
from caixa.serializer import CaixaSerializer


class CaixaViewSet(viewsets.ModelViewSet):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer
