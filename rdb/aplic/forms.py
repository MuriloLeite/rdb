from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Feedback, Comentario

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['texto']
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']