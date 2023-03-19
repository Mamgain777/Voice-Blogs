from django.urls import path
from main import views


app_name = 'main'

urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    # path('login',views.LoginPage.as_view(), name='login'),
    path('register',views.register_user, name='register'),
    path('about',views.about_page, name='about'),
    path('<str:user>/create-profile',views.profile_save, name='profile')
]