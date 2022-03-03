from rest_framework import serializers
from emeil.models import Emeil


class EmeilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emeil
        fields = "__all__"
