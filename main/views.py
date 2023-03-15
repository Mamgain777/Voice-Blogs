from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from main.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from user.models import Blog,Category

# Create your views here.

class HomePage(generic.ListView):
    
    model = Blog
    context_object_name = 'blogs'
    template_name = 'main/home.html'

    def get_context_data(self,*args, **kwargs):
        contex =  super(HomePage,self).get_context_data(*args,**kwargs)
        contex['cat_list'] = Category.objects.all()
        
        return contex

    def get_queryset(self, *args,**kwargs):
        
        return Blog.objects.all().filter(publish_date__isnull=False).order_by('-publish_date')


class RegisterPage(generic.CreateView):
    
    template_name = 'main/register.html'
    form_class = CustomUserCreationForm
    # fields = ('username','email','password','first_name','last_name')
    success_url = reverse_lazy('login')

# class LoginPage(generic.TemplateView):
    
#     template_name = 'main/login.html'