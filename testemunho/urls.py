from django.urls import path

from .views import ComentarioAPIView, ComentariosAPIView, TestemunhoAPIView, TestemunhosAPIView

urlpatterns = [
    path('testemunhos/', TestemunhosAPIView.as_view(), name='testemunhos'),
    path('comentarios/', ComentariosAPIView.as_view(), name='comentarios'),
    path('testemunhos/<int:pk>/', TestemunhoAPIView.as_view(), name='testemunho'),
    path('comentarios/<int:pk>/', ComentarioAPIView.as_view(), name="comentario")
]