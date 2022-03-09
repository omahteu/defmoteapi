from rest_framework import serializers
from caixa.models import Caixa


class CaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caixa
        fields = "__all__"
