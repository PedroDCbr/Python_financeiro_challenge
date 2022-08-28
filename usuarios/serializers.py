from .models import Usuario
from rest_framework import serializers
from despesas.models import Despesas
from receitas.models import Receitas


class UsuarioSerializer(serializers.ModelSerializer):
    despesas = serializers.PrimaryKeyRelatedField(many=True, queryset=Despesas.objects.all())
    receitas = serializers.PrimaryKeyRelatedField(many=True, queryset=Receitas.objects.all())

    def create(self, validated_data):
        usuario = Usuario.objects.create(**validated_data)
        return usuario

    class Meta:
        model = Usuario
        exclude = []
