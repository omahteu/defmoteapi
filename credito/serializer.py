from rest_framework import serializers
from credito.models import Credito


class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = "__all__"
