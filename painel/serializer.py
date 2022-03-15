from rest_framework import serializers
from painel.models import Painel


class PainelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painel
        fields = "__all__"
