from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, phone=None):
        user = self.model(
            email=email,
            username=username,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, phone=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            phone=phone
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE, null=True, default="")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    

class Pessoafisica(CustomUser):
    cpf = models.CharField(max_length=14)

    class Meta:
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

    def __str__(self):
        return (self.cpf)
class Pessoajuridica(CustomUser):
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
    numero = models.IntegerField()
    descricao = models.TextField(null=True)
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __str__(self):
        return f"{self.nomeOrganizador}, {self.data}, {self.cep}, {self.numero}, {self.descricao}"
class Feedback(models.Model):
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
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
    telefone = models.IntegerField()
    class Meta:
        verbose_name = 'Parceria'
        verbose_name_plural = 'Parcerias'

    def __str__(self):
        return f"{self.nome},{self.email},{self.telefone}"
    
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
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
    def __str__(self):
        return f'Comentario por {self.autor} em {self.data_publicacao}'

class Endereco(models.Model):
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=60)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=70, blank=True)
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
class Doacao(models.Model):
    valor = models.IntegerField()
    doador = models.ForeignKey('CustomUser',on_delete=models.SET_NULL,null=True)
    item = models.TextField(max_length=100)
    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'