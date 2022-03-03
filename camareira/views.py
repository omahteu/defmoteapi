from rest_framework import viewsets
from camareira.models import Camareira
from camareira.serializer import CamareiraSerializer


class CamareiraViewSet(viewsets.ModelViewSet):
    queryset = Camareira.objects.all()
    serializer_class = CamareiraSerializer
