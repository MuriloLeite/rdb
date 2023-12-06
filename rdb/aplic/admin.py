from django.contrib import admin
from aplic.models import  Pessoafisica, Doacao, Pessoajuridica, Imagem, Feedback,Comentario, Evento, Parceria, Atracao, Equipamento


@admin.register(Pessoafisica)
class PessoafisicaAdmin(admin.ModelAdmin):
    list_display = ['cpf']
    search_fields = ['texto']
@admin.register(Pessoajuridica)
class PessoajuridicaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'nomeFantasia', 'razaoSocial')  
    search_fields = ['texto']
@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    search_fields = ['texto']
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display =['evento']
    search_fields = ['texto']
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    search_fields = ['texto']
@admin.register(Parceria)
class ParceriaAdmin(admin.ModelAdmin):
    search_fields = ['texto']
@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    search_fields = ['texto']
@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ['atracao', 'texto']
    search_fields = ['texto']
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['texto', 'data_publicacao', 'imagem']
    list_filter = ['data_publicacao']
    search_fields = ['texto']
@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ['valor']
    search_fields = ['texto']
