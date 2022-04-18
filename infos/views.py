from rest_framework import viewsets
from infos.models import Infos
from infos.serializer import InfosSerializer


class InfosViewSet(viewsets.ModelViewSet):
    queryset = Infos.objects.all()
    serializer_class = InfosSerializer
