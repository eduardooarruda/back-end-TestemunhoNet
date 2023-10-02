from django.urls import path

from .views import ComentarioAPIView, ComentariosAPIView, TestemunhoAPIView, TestemunhosAPIView

urlpatterns = [
    path('testemunhos/', TestemunhosAPIView.as_view(), name='testemunhos'),
    path('testemunhos/<int:pk>/', TestemunhoAPIView.as_view(), name='testemunho'),

    path('testemunhos/<int:testemunho_pk>/comentarios/', ComentariosAPIView.as_view(), name='testemunho_comentarios'),
    path('testemunhos/<int:testemunho_pk>/comentarios/<int:comentario_pk>/', ComentarioAPIView.as_view(), name='testemunho_comentario'),

    path('comentarios/', ComentariosAPIView.as_view(), name='comentarios'),
    path('comentarios/<int:comentario_pk>/', ComentarioAPIView.as_view(), name="comentario")
]