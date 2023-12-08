from django.contrib import admin
from .models import Testemunho, Comentario, Like



# @admin.register(Usuario)
# class UsuarioAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'email')
#     search_fields = ('nome',)

@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo', 'data_criacao', 'autor', 'comentarios_ativo', 'quantidade_comentarios', 'quantidade_likes')
    search_fields = ('titulo',)
    list_filter = ('comentarios_ativo',)

    @admin.display(description="Quantidade de comentários")
    def quantidade_comentarios(self, obj):
        return obj.comentarios.count()
    
    @admin.display(description="Quantidade de likes")
    def quantidade_likes(self, obj):
        return obj.likes.count()


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'testemunho', 'conteudo', 'data_criacao')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'testemunho')
