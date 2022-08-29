from rest_framework import views, response
from .models import Resumo
from receitas.models import Receitas
from despesas.models import Despesas


class Resumo(views.APIView):
    queryset = Resumo.objects.all()

    def get_saldo_mes(self, ano, mes):
        receita_mes = self.get_receita_mes(ano, mes)
        despesas_mes = self.get_despesa_mes(ano, mes)
        saldo = receita_mes - despesas_mes
        return saldo

    def get_despesa_mes(self, ano, mes):
        total = 0
        if ano or mes != '':
            despesas = Despesas.objects.filter(data__contains=f'{ano}-{mes}')
            for valor in despesas:
                total += valor.valor
            return total
        else:
            raise ValueError(f'Não a despesas em {mes}/{ano}')

    def get_receita_mes(self, ano, mes):
        total = 0
        if ano or mes != '':
            receita = Receitas.objects.filter(data__contains=f'{ano}-{mes}')
            for v in receita:
                total += v.valor
            return total
        else:
            raise ValueError(f'Não a receita em {mes}/{ano}')

    def get_categoria(self):
        return {
            'Outros': 0,
            'Moradia': 0,
            'Transporte': 0,
            'Alimentação': 0,
            'Cartões': 0,
            'Educação': 0,
            'Saúde': 0,
            'Imprevistos': 0,
            'Lazer': 0,
        }

    def get_total_despesas_por_categoria(self, ano, mes):
        despesas = Despesas.objects.filter(data__contains=f'{ano}-{mes}')
        categoria = self.get_categoria()
        for cats in despesas:
            categoria[cats.categorias] += cats.valor
        return categoria

    def get(self, request, ano, mes):
        receitas = self.get_receita_mes(ano, mes)
        despesas = self.get_despesa_mes(ano, mes)
        saldo_do_mes = receitas - despesas
        despeses_por_categoria = self.get_total_despesas_por_categoria(ano, mes)
        return response.Response(
            data={
                f'Total receitas de {mes}/{ano}': f'{receitas:.2f}',
                f'Total despesas de {mes}/{ano}': f'{despesas:.2f}',
                f'Saldo total de {mes}/{ano}': f'{saldo_do_mes:.2f}',
                f'Despesas por categoria de de {mes}/{ano}': despeses_por_categoria
            }
        )
