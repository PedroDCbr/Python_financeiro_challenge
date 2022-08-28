from django.contrib import admin
from .models import Receitas


class Receita(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id',)
    search_fields = ('id', 'descricao', 'valor', 'data')
    ordering = ('descricao', 'valor', 'data')
    list_per_page = 20


admin.site.register(Receitas, Receita)