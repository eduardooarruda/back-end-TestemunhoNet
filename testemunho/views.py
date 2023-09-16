from rest_framework import generics

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

class ComentarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer