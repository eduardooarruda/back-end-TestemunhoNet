from rest_framework import serializers
from .models import Testemunho, Comentario

class TestemunhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testemunho
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'