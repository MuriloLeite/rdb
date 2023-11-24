from django import forms
from django.contrib.auth.models import User
from .models import Feedback

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['texto']