from rest_framework import serializers
from comanda.models import Comanda


class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = "__all__"
