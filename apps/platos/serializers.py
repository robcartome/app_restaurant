from rest_framework import serializers
from apps.platos.models import Platos


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = '__all__'