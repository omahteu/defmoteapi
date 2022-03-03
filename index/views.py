from rest_framework import viewsets
from index.models import Dados
from index.serializer import DadosSerializer


class DadosViewSet(viewsets.ModelViewSet):
    queryset = Dados.objects.all()
    serializer_class = DadosSerializer
