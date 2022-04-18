from rest_framework import viewsets
from infos.models import Cabeca
from infos.serializer import CabecaSerializer


class CabecaViewSet(viewsets.ModelViewSet):
    queryset = Cabeca.objects.all()
    serializer_class = CabecaSerializer
