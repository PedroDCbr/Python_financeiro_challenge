from rest_framework import viewsets, generics
from .models import Receitas
from .serializers import ReceitasSerializer


class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Receitas"""
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer
    filterset_fields = ['descricao']


class ListaReceitasPorData(generics.ListAPIView):
    """Listando Despesas por Ano e Mes"""
    serializer_class = ReceitasSerializer

    def get_queryset(self):
        queryset = Receitas.objects.filter(data__year=self.kwargs['ano'])
        return queryset

    def get_queryset(self):
        queryset = Receitas.objects.filter(data__month=self.kwargs['mes'])
        return queryset

