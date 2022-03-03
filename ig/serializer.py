from rest_framework import serializers
from ig.models import Ig


class IgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ig
        fields = '__all__'
