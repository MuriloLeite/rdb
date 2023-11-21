from django.urls import path
from .views import IndexView, ContatoView, ParceriasView, EventosView, registro, EventoDetailView, adicionar_comentario, adicionar_feedback, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("registro/", registro, name="registro"),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path("parcerias", ParceriasView.as_view(), name="parcerias"),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('evento/<int:pk>/', EventoDetailView.as_view(), name='evento-detalhes'),
    path('adicionar_feedback/<int:evento_id>/', adicionar_feedback, name='adicionar_feedback'),
    path('adicionar_comentario/<int:imagem_id>/<int:evento_id>/', adicionar_comentario, name='adicionar_comentario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
