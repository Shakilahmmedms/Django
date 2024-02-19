from django.urls import path
from .import views

urlpatterns = [
    path('',views.add_categorie, name='add_categorie')
]
