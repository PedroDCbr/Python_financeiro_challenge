from django.db import models
from django.contrib.auth.models import User


class Receitas(models.Model):
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=50, decimal_places=2)
    data = models.DateField(blank=False, null=False)
    TAG = (
        ('O', 'Outros'),
        ('S', 'Salário'),
        ('E', 'Extras'),
        ('B', 'Bonificação')
    )
    categorias = models.CharField(max_length=1, default='O', choices=TAG,  blank=False, null=False)
