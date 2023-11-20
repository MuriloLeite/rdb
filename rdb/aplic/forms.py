from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Feedback, Comentario

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone', 'password']

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Por favor, entre com um username e senha corretos. Note que ambos os campos diferenciam maiúsculas e minúsculas.',
        'inactive': 'Esta conta está inativa.',
    }

class LoginForm(forms.Form):        
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['texto']