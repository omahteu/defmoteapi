from rest_framework import serializers
from camareira.models import Camareira


class CamareiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camareira
        fields = '__all__'
