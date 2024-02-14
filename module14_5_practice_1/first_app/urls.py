from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('contact_form/', views.conact_form, name='contact_form'),

]
