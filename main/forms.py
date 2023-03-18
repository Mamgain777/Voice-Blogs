from django import forms
# from main.models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import UserProfile



class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form form-control'}),label="Password",max_length=30)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form form-control'}),label="Confirm Password",max_length=30)


    class Meta:
        model = User
        fields = ('username',)

        help_texts = {
            'username': "",
        }

    def __init__(self, *args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form form-control'
            

class UserProfileForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ('email','profile_pic','first_name','last_name','description')

        widgets = {
            'email': forms.TextInput(attrs={
            'class': 'form form-control',
            }),
            'first_name': forms.TextInput(attrs={
            'class': 'form form-control',
            }),
            'last_name': forms.TextInput(attrs={
            'class': 'form form-control',
            }),
            'profile_pic': forms.FileInput(attrs={
            'class': 'form form-control',
            }),
            'description': forms.Textarea(attrs={
            'class': 'form form-control',
            }),
        }

        