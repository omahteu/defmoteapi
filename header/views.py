from rest_framework import viewsets
from header.models import Cabeca
from header.serializer import CabecaSerializer


class CabecaViewSet(viewsets.ModelViewSet):
    queryset = Cabeca.objects.all()
    serializer_class = CabecaSerializer
