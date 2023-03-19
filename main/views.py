from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from main.forms import CustomUserCreationForm,UserProfileForm
from django.urls import reverse_lazy, reverse
from user.models import Blog,Category,UserProfile

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


def register_user(request):

    form = CustomUserCreationForm()
    if request.method == "POST":
        print("Check point 1")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save()
            user.save()
            return HttpResponseRedirect(reverse('main:profile',kwargs={'user':username}))

    
    return render(request,'registration/register.html',{'form':form})

class ProfileView(generic.CreateView):
    model = UserProfile
    template_name = 'user/profileEdit.html'
    # fields = ('title','content')
    form_class = UserProfileForm
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        user = User.objects.filter(username = self.kwargs['user'])[0]
        form.instance.user = user
        return super().form_valid(form)
    
def profile_save(request,user):

    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            user_is = User.objects.filter(username=user)[0]
            profile.user = user_is

            if 'profile_pic' in request.FILES:
                print('Found It!')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            return HttpResponseRedirect(reverse('login'))
        
    user = User.objects.filter(username=user)[0]
    if user == []:
        form = UserProfileForm()
        return render(request,'user/profileCreate.html', {'form':form,'user':user})
    else:
        return render(request,'main/error.html')


def about_page(request):
    return render(request, 'main/about.html')
