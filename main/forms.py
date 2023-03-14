from django import forms
# from main.models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form form-control'}), max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form form-control'}),max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form form-control'}),label="Password",max_length=30)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form form-control'}),label="Confirm Password",max_length=30)


    class Meta:
        model = User
        fields = ('username','email' ,'first_name', 'last_name')

        help_texts = {
            'username': "",
            'password1': ""
        }

        

        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'form form-control',
            }),
            
        }

        