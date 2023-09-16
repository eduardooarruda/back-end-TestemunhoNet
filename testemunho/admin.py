from django.contrib import admin

from .models import Testemunho, Comentario


@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo', 'dataCriacao', 'autor', 'comentariosAtivo')

@admin.register(Comentario)
class ComentarioAdimin(admin.ModelAdmin):
    list_display = ('testemunho', 'autor', 'conteudo')