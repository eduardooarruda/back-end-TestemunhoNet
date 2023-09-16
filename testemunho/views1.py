from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Testemunho, Comentario
from .serializers import TestemunhoSerializer, ComentarioSerializer

class TestemunhoAPIView(APIView):
    """
    Todos os testemunhos
    """

    def get(self, request):
        testemunhos = Testemunho.objects.all()
        serializer = TestemunhoSerializer(testemunhos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TestemunhoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ComentarioAPIView(APIView):
    """
    Todos os comentários
    """
    def get(self, resquest):
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ComentarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)