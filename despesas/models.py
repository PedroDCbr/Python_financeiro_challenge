from django.db import models
from django.contrib.auth.models import User


class Despesas(models.Model):
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=50, decimal_places=2, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    TAG = (
        ('O', 'Outros'),
        ('M', 'Moradia'),
        ('T', 'Transporte'),
        ('A', 'Alimentação'),
        ('C', 'Cartões'),
        ('E', 'Educação'),
        ('S', 'Saúde'),
        ('I', 'Imprevistos'),
        ('L', 'Lazer'),
    )
    categorias = models.CharField(max_length=1, choices=TAG, blank=False, null=False, default='O')
