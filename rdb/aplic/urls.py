from django.urls import path
from .views import IndexView, ContatoView, CustomLoginView, ParceriasView, EventosView, registro, user_login, EventoDetailView, adicionar_feedback, adicionar_comentario
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("registro/", registro, name="registro"),
    path('login/', user_login, name='user_login'),
    path("parcerias", ParceriasView.as_view(), name="parcerias"),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('evento/<int:pk>/', EventoDetailView.as_view(), name='evento-detalhes'),
    path('adicionar_feedback/<int:evento_id>/', adicionar_feedback, name='adicionar_feedback'),
    path('adicionar_comentario/<int:imagem_id>/', adicionar_comentario, name='adicionar_comentario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)