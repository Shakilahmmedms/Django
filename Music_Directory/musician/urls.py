from django.urls import path
from .import views

urlpatterns = [
    path('musician/',views.create_musician, name='create_musician')
]


