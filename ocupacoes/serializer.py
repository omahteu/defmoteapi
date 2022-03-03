from rest_framework import serializers
from ocupacoes.models import Ocupacao


class OcupacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocupacao
        fields = "__all__"
