from django import forms
# from main.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.ModelForm):
    
    class Meta():
        model = User
        fields = ('username','email','password','first_name')

        labels = {
            'username':'',
            'password':'',
            'email':''
        }

        widgets = {
            "username": forms.TextInput(attrs={
            'class':"form-control",
            'placeholder': "Enter Username"
            }),
            "email": forms.EmailInput(attrs={
            'class':"form-control",
            'placeholder': "Enter Email"
            }),
            "password": forms.PasswordInput(attrs={
            'class':"form-control",
            'placeholder': "Enter Password"
            })
        }
        help_texts = {
            'username':None
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1','password2')

        

        labels = {
            'username': "",
            'password1': "",
            'password2': "",
        }

        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

