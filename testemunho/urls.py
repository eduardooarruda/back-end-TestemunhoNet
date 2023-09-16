from django.urls import path

from .views import ComentarioAPIView, TestemunhoAPIView

urlpatterns = [
    path('testemunhos/', TestemunhoAPIView.as_view(), name='testemunhos'),
    path('comentarios/', ComentarioAPIView.as_view(), name='comentarios'),
]