from rest_framework import generics

from .models import Testemunho, Comentario
from .serializers import TestemunhoSerializer, ComentarioSerializer

class TestemunhoAPIView(generics.ListCreateAPIView):
    queryset = Testemunho.objects.all()
    serializer_class = TestemunhoSerializer

class ComentarioAPIView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
