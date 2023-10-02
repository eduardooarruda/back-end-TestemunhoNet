from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Testemunho, Comentario
from .serializers import TestemunhoSerializer, ComentarioSerializer

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
    