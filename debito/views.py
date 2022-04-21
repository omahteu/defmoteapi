from rest_framework import viewsets
from debito.models import Debito
from debito.serializer import DebitoSerializer


class DebitoViewSet(viewsets.ModelViewSet):
    queryset = Debito.objects.all()
    serializer_class = DebitoSerializer
