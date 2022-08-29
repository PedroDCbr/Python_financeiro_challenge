from django.db import models
from django.contrib.auth.models import User


class Enum(models.TextChoices):
    Outros = 'Outros'
    Salario = 'Salário'
    Extras = 'Extras'
    Bonificacao = 'Bonificação'


class Receitas(models.Model):
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=50, decimal_places=2)
    data = models.DateField(blank=False, null=False)
    categorias = models.CharField(max_length=11, choices=Enum.choices, blank=False, default=Enum.Outros)
