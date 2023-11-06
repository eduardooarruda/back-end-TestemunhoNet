from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Testemunho(models.Model):
    titulo = models.CharField(max_length=300)
    conteudo = models.CharField(max_length=3000)
    data_criacao = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Usuario, related_name="testemunhos", on_delete=models.CASCADE)
    comentarios_ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'testemunho'
        verbose_name_plural = 'testemunhos'
        ordering = ['id']

    def __str__(self) -> str:
        return self.titulo
    

class Comentario(models.Model):
    data_criacao = models.DateTimeField(auto_now=True)
    conteudo = models.CharField(max_length=1000)
    testemunho = models.ForeignKey(Testemunho, related_name="comentarios", on_delete=models.CASCADE)
    comentario_pai = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, related_name="comentarios", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'
        ordering = ['id'] #ordernação crescente
        #ordering = ['-id'] #ordernação decrescente
        

    def __str__(self) -> str:
        return f'{self.autor} comentou no testemunho {self.testemunho}'

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    testemunho = models.ForeignKey(Testemunho, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'testemunho')

    def __str__(self):
        return f'{self.usuario} curtiu o testemunho {self.testemunho}'