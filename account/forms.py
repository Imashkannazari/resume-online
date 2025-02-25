from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        username = forms.CharField(max_length=100, required=True)
        email = forms.EmailField(max_length=100, required=True)
        password1 = forms.CharField(max_length=100, required=True)
        
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        
        model = CustomUser
        fields = ['username', 'password']