from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    # path('profile/',views.UserLoginView.as_view(), name='login'),
    # path('',views.signup, name='signup'),
]
