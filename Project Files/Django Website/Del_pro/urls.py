"""Del_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from login import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('detail/',views.detail),
    path('forget_pass/',views.forget_pass),
    path('register/', views.register),
    path('register2/', views.register2, name='register2'),
    path('login/', include('login.urls')),
    path('home/', views.home),
    path('homein/', auth_views.LoginView.as_view(template_name='login/homein.html'),name='login'),
    path('homeout/', auth_views.LogoutView.as_view(template_name='login/homeout.html'),name='logout'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile,name='profile'),
    path('', views.home)

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

