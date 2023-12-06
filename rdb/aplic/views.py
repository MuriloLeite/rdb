from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .forms import FeedbackForm
from .models import Evento, Feedback, Imagem, Comentario, Parceria, Pessoa
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
class IndexView(TemplateView):
    template_name = 'index.html'
class GaleriaView(TemplateView):
    template_name = 'galeria.html'
class ContatoView(TemplateView):
    template_name = 'contato.html'
class DoacaoView(TemplateView):
    template_name = "doacao.html"

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
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        username = request.POST.get("username")
        password = request.POST.get("senha")

        # Verifique se o campo 'username' está definido
        if username:
            # Verifique se o username já existe
            if User.objects.filter(username=username).exists():
                messages.error(request, 'O nome de usuário já existe. Escolha outro.')
                return redirect('registro')

            # Criação do usuário e pessoa se o username não existir
            user_instance = User.objects.create_user(username=username, password=password)
            pessoa_instance = Pessoa.objects.create(nome=nome, cpf=cpf, user=user_instance)
            user_instance.save()
            pessoa_instance.save()

            # Adiciona uma mensagem de sucesso
            messages.success(request, 'Registro bem-sucedido. Faça login para continuar.')

            return redirect('login')
        else:
            # Adiciona uma mensagem de erro se o campo 'username' não for preenchido
            messages.error(request, "O campo 'username' deve ser preenchido.")
            return redirect('registro')
    else:
        # Lógica para renderizar o formulário HTML
        return render(request, "registro.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('http://127.0.0.1:8000/')  # Redirecione para a página de dashboard ou outra página desejada após o login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


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
        pass

class MeusDadosView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'meusdados.html')
    
def parcerias(request):
    parcerias = Parceria.objects.all()
    return render(request, 'parcerias.html', {'parcerias': parcerias})

def eventos(request):
    search_term = request.GET.get('search', '')
    print(f"Termo de pesquisa: {search_term}")
    eventos = Evento.objects.filter(nomeOrganizador__icontains=search_term)
    return render(request, 'eventos.html', {'eventos': eventos, 'search_term': search_term})