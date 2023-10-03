from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Testemunho, Comentario
from .serializers import TestemunhoSerializer, ComentarioSerializer


"""
API V1
"""
# ListCreateAPIView: tanto lista quanto criar não depende de nenhum id
class TestemunhosAPIView(generics.ListCreateAPIView):
    queryset = Testemunho.objects.all()
    serializer_class = TestemunhoSerializer

# RetrieveUpdateDestroyAPIView: tanto pegar um ..., quanto atualizar ou deletar depende de um id 
class TestemunhoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testemunho.objects.all()
    serializer_class = TestemunhoSerializer

class ComentariosAPIView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        if self.kwargs.get('testemunho_pk'):
            return self.queryset.filter(testemunho_id=self.kwargs.get('testemunho_pk'))
        return self.queryset.all()

class ComentarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_object(self):
        if self.kwargs.get('testemunho_pk'):
            return get_object_or_404(self.get_queryset(), 
                                     testemunho_id=self.kwargs.get('testemunho_pk'),
                                     pk=self.kwargs.get('comentario_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('comentario_pk'))
    


"""
API V2
"""

class TestemunhoViewSet(viewsets.ModelViewSet):
    queryset = Testemunho.objects.all()
    serializer_class = TestemunhoSerializer

    
    @action(detail=True, methods=['get'])
    def comentarios(self, request, pk=None):
        #pega o testemunho que esta chamando
        testemunho = self.get_object()
        serializer = ComentarioSerializer(testemunho.comentarios.all(), many=True)
        return Response(serializer.data)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
