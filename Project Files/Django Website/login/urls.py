
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('detail/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('register2/', views.register2, name='register2'),
    path('forget_pass/', views.forget_pass, name='forget_pass'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    # path('homeout/', views.home, name='logout'),
    path('homein/', auth_views.LoginView.as_view(template_name='login/homein.html'), name='login'),
    path('homeout/', auth_views.LogoutView.as_view(template_name='login/homeout.html'), name='logout'),
    path('', views.home),
]