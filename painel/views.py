from rest_framework import viewsets
from painel.models import Painel
from painel.serializer import PainelSerializer


class PainelViewSet(viewsets.ModelViewSet):
    queryset = Painel.objects.all()
    serializer_class = PainelSerializer
