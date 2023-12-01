from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
# from rest_framework import permissions

from rest_framework.decorators import action
from django.contrib.auth.models import User

from .models import Testemunho, Comentario
from .serializers import TestemunhoSerializer, ComentarioSerializer, UserSerializer
# from .permissions import EhSuperUsuario

# ListCreateAPIView vem junto porque não depende de nenhum id para ser executado
# RetrieveUpdateDestroyAPIView vem junto porque depende de um id para executar a ação

"""
API V1
"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        return Response({'user': UserSerializer(user).data})

    def perform_create(self, serializer):
        return serializer.save()
    
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
    #permission_classes = (EhSuperUsuario, 
    #                      permissions.DjangoModelPermissions, )
    queryset = Testemunho.objects.all()
    serializer_class = TestemunhoSerializer

    
    @action(detail=True, methods=['get'])
    def comentarios(self, request, pk=None):
        self.pagination_class.page_size = 1
        comentarios = Comentario.objects.filter(testemunho_id=pk)
        page = self.paginate_queryset(comentarios)

        if page is not None:
            serializer = ComentarioSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        #pega o testemunho que esta chamando
        # testemunho = self.get_object()

        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

"""
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
"""

#O retrieve pega um registro
#Destroy deleta um registro
class ComentarioViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer