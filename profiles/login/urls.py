from django.urls import path
from .import views
from .import django_form
urlpatterns = [

    path('', views.loginHome, name='home'),
    path('form/', views.loginForm, name='form'),
    path('django_form/', views.djangoForm,name='django_form')
]