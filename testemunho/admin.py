from django.contrib import admin
from .models import Usuario, Testemunho, Comentario, Like

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo', 'data_criacao', 'autor', 'comentarios_ativo')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'testemunho', 'conteudo', 'data_criacao')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'testemunho')
