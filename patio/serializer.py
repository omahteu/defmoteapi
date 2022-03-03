from rest_framework import serializers
from patio.models import Patio


class PatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patio
        fields = "__all__"
