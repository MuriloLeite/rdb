from django.urls import path
from .views import IndexView, ContatoView, ParceriasView, EventosView, DoacaoView, registro, EventoDetailView, adicionar_comentario, adicionar_feedback
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from aplic.forms import UserLoginForm
from django.contrib.auth import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("doacao/", DoacaoView.as_view(), name="doacao"),
    path("registro/", registro, name="registro"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path("parcerias", ParceriasView.as_view(), name="parcerias"),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('evento/<int:pk>/', EventoDetailView.as_view(), name='evento-detalhes'),
    path('adicionar_feedback/<int:evento_id>/', adicionar_feedback, name='adicionar_feedback'),
    path('adicionar_comentario/<int:imagem_id>/<int:evento_id>/', adicionar_comentario, name='adicionar_comentario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
