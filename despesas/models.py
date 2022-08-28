from django.db import models
from usuarios.models import Usuario


class Despesas(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='despesas', on_delete=models.CASCADE, default='', null=True, blank=True)
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
