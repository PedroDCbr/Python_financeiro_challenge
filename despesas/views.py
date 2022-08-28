from rest_framework import viewsets, generics
from .models import Despesas
from .serializers import DespesaSerializer, ListaDespesasPorAnoEMesSerializer

class DespesasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Despesas"""
    queryset = Despesas.objects.all()
    serializer_class = DespesaSerializer
    filterset_fields = ['descricao']


class ListaDespesasPorData(generics.ListAPIView):
    """Listando Despesas por Ano e Mes"""
    serializer_class = ListaDespesasPorAnoEMesSerializer

    def get_queryset(self):
        ano = Despesas.objects.filter(data__year=self.kwargs['ano'])
        return ano

    def get_queryset(self):
        mes = Despesas.objects.filter(data__month=self.kwargs['mes'])
        return mes

