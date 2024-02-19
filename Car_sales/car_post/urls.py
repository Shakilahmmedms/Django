from django.urls import path
from .import views
urlpatterns = [
    path('',views.Car_list, name='add_car')
]
