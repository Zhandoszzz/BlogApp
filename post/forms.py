from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Login", widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label="Repeat password", widget = forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ("username","password1","password2")

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username","password")

class AddCommentForm(forms.ModelForm):
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control','rows':"3",'placeholder':"Add a comment..."}))
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddCommentForm, self).__init__(*args, **kwargs)

