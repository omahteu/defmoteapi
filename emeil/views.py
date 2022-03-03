from rest_framework import viewsets
from emeil.models import Emeil
from emeil.serializer import EmeilSerializer


class EmeilViewSet(viewsets.ModelViewSet):
    queryset = Emeil.objects.all()
    serializer_class = EmeilSerializer
