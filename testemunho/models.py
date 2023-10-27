from django.db import models

# Create your models here.

class Testemunho(models.Model):
    titulo = models.CharField(max_length=300)
    conteudo = models.CharField(max_length=3000)
    dataCriacao = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100)
    comentariosAtivo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'testemunho'
        verbose_name_plural = 'testemunhos'
        ordering = ['id']

    def __str__(self) -> str:
        return self.titulo
    

class Comentario(models.Model):
    testemunho = models.ForeignKey(Testemunho, related_name="comentarios", on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=600)

    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'
        ordering = ['id'] #ordernação crescente
        #ordering = ['-id'] #ordernação decrescente

    def __str__(self) -> str:
        return f'{self.autor} comentou no testemunho {self.testemunho}'

