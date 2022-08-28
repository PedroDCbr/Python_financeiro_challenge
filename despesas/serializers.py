from rest_framework import serializers
from .models import Despesas


class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = '__all__'


class ListaDespesasPorAnoEMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = '__all__'
