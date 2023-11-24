from rest_framework import serializers
from .models import Testemunho, Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = (
            'id',
            'testemunho',
            'autor',
            'conteudo',
            'comentario_pai',
        )

class TestemunhoSerializer(serializers.ModelSerializer):
    # read_only = Somente leitura
    # many = Um testemunho pode ter vários comentários
    #comentarios = ComentarioSerializer(many=True, read_only=True) #Nested Relationship

    #OBS: Têm que ser detail, porque estou utilizando ViewSet
    # comentarios = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comentario-detail') #HyperLinked Related Field
    comentarios = serializers.PrimaryKeyRelatedField(many=True, read_only=True)#Primary Key Related Field
    likes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Testemunho
        fields =  (
            'id',
            'titulo',
            'conteudo', 
            'data_criacao', 
            'autor', 
            'comentarios_ativo',
            'comentarios',
            # 'likes',
            'likes_count',
        )

    def get_likes_count(self, obj):
        return obj.likes.count()

