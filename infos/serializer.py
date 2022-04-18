from rest_framework import serializers
from infos.models import Cabeca


class CabecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabeca
        fields = "__all__"
