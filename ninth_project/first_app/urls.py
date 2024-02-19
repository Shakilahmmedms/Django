from django.urls import path
from .import views

urlpatterns = [
    path('', views.set_session, name='home'),
    path('get/', views.get_session, name='get_cookies'),
    path('delete/', views.delet_session, name='delet_cookies'),
]
