from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import TemplateView, ListView, DetailView
from .forms import CustomUserCreationForm, FeedbackForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .models import Evento, Feedback, Imagem, Comentario
from django.views.decorators.http import require_POST

class IndexView(TemplateView):
    template_name = 'index.html'
class GaleriaView(TemplateView):
    template_name = 'galeria.html'
class ContatoView(TemplateView):
    template_name = 'contato.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
class RegistroView(TemplateView):
    template_name = 'registro.html'
class ParceriasView(TemplateView):
    template_name = 'parcerias.html'
class EventosView(TemplateView):
    template_name = 'eventos.html'

class EventosView(ListView):
    model = Evento
    template_name = 'eventos.html'
    context_object_name = 'eventos'
class EventoDetailView(DetailView):
    model = Evento
    template_name = 'evento_detalhes.html'  # Crie este template posteriormente
    context_object_name = 'evento'


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('login'))
        else:
            return render(request, 'registro.html', {'form': form, 'error_message': 'O formulário não é válido.'})
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
@require_POST
def adicionar_feedback(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.evento = evento
            feedback.autor = request.user
            feedback.save()

            # Redirecione para a página de detalhes do evento
            return redirect('evento-detalhes', pk=evento_id)
        else:
            return redirect('evento-detalhes', pk=evento_id)
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.filter(evento=evento)
    return render(request, 'aplic/adicionar_feedback.html', {'form': form, 'evento': evento, 'feedbacks': feedbacks})

    



def adicionar_comentario(request, imagem_id, evento_id):
    if request.method == 'POST':
        imagem = get_object_or_404(Imagem, pk=imagem_id)
        texto = request.POST.get('texto')
        autor = request.user
        Comentario.objects.create(imagem=imagem, autor=autor, texto=texto)
        return redirect('evento-detalhes', pk=evento_id)
    else:
        # Adicione o código para lidar com métodos de requisição diferentes, se necessário  
        pass