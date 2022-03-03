from rest_framework import viewsets
from produto.models import Produto
from produto.serializer import ProdutoSerializer


class ProdutoViewSets(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
