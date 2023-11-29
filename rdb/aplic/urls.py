from django.urls import path
from .views import IndexView, ContatoView, parcerias, MeusDadosView, eventos, DoacaoView, registro, EventoDetailView, adicionar_comentario, adicionar_feedback, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("doacao/", DoacaoView.as_view(), name="doacao"),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('parcerias/', parcerias, name='pagina_parcerias'),
    path('eventos/', eventos, name='eventos'),
    path('evento/<int:pk>/', EventoDetailView.as_view(), name='evento-detalhes'),
    path('adicionar_feedback/<int:evento_id>/', adicionar_feedback, name='adicionar_feedback'),
    path('adicionar_comentario/<int:imagem_id>/<int:evento_id>/', adicionar_comentario, name='adicionar_comentario'),
    path('meus-dados/', MeusDadosView.as_view(), name='meus_dados'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
