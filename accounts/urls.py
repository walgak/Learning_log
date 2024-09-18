from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.xhtml'), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name = 'register'),
]