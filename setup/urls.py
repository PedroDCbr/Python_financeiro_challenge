from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from receitas.views import ReceitasViewSet, ListaReceitasPorData
from despesas.views import DespesasViewSet, ListaDespesasPorData
from resumo.views import Resumo
from usuarios.views import UsuarioViewSet

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='receitas')
router.register('despesas', DespesasViewSet, basename='despesas')
router.register('usuario', UsuarioViewSet, basename='usuario')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('despesas/<int:ano>/<int:mes>', ListaDespesasPorData.as_view()),
    path('receitas/<int:ano>/<int:mes>', ListaReceitasPorData.as_view()),
    path('resumo/<str:ano>/<str:mes>', Resumo.as_view()),
]
