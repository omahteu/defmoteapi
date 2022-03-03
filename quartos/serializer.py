from rest_framework import serializers
from quartos.models import Quarto


class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = "__all__"
