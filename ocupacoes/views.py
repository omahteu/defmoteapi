from rest_framework import viewsets
from ocupacoes.models import Ocupacao
from ocupacoes.serializer import OcupacaoSerializer


class OcupacaoViewSet(viewsets.ModelViewSet):
    queryset = Ocupacao.objects.all()
    serializer_class = OcupacaoSerializer
