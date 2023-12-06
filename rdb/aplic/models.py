from django.db import models
from django.contrib.auth.models import BaseUserManager, User



class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=32, null=True)
    cpf = models.CharField(max_length=14, default='')

class Pessoafisica(Pessoa):

    class Meta:
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

    def __str__(self):
        return (self.cpf)
class Pessoajuridica(Pessoa):
    cnpj = models.CharField(max_length=18)
    razaoSocial = models.CharField(max_length=100)
    nomeFantasia = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'

    def __str__(self):
        return f"{self.razaoSocial}, {self.nomeFantasia}"

class Evento(models.Model):
    nomeOrganizador = models.CharField(max_length=30)
    data = models.DateField()
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=50, default='')
    descricao = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='event_images/', blank=True, null=True)
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __str__(self):
        return f"{self.nomeOrganizador}, {self.data}"
    
class Feedback(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    texto = models.TextField(max_length=200)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, default=None)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
    def __str__(self):
        return f'Feedback por {self.autor} em {self.data_criacao}'
class Imagem(models.Model):
    formato = models.ImageField(upload_to='event_images/', blank=True, null=True)
    legenda = models.CharField(max_length=50)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, default=None)
    class Meta:
        verbose_name = 'Imagem' 
        verbose_name_plural = 'Imagens'
    def __str__(self):
        return (self.legenda)
    
class Parceria(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=20)  # Alterado para CharField

    class Meta:
        verbose_name = 'Parceria'
        verbose_name_plural = 'Parcerias'

    def __str__(self):
        return f"{self.nome}, {self.email}, {self.telefone}"

    
class Atracao(models.Model):
    texto = models.TextField(max_length=100, default="")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, default=None)
    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
    def __str__(self):
        return (self.texto) 
class Equipamento(models.Model):
    texto = models.TextField(max_length=100,  default="")
    atracao = models.ForeignKey(Atracao, on_delete=models.CASCADE, null=True, default=None)
    def __str__(self):
        return (self.texto)
    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
    
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
    def __str__(self):
        return f'Comentario por {self.autor} em {self.data_publicacao}'

class Doacao(models.Model):
    valor = models.IntegerField()
    doador = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    item = models.TextField(max_length=100)
    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'