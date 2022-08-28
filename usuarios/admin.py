from django.contrib import admin
from .models import Usuario


class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active')
    list_display_links = ('id', 'username')


admin.site.register(Usuario, Usuarios)
