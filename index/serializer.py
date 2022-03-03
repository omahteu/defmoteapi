from rest_framework import serializers
from index.models import Dados


class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = '__all__'
