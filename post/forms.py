from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Login", widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label="Repeat password", widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username","password1","password2")

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username","password1")

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'