from rest_framework import serializers
from debito.models import Debito


class DebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debito
        fields = "__all__"
