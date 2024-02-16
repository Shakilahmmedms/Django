from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home, name='hompage'),
    path('signup/',views.signup, name='signup_page'),
    path('login/',views.user_login, name='login_page'),
    path('logout/',views.user_logout, name='logout_page'),
    path('pass_change/',views.pass_change, name='pass_change'),
    path('pass_change2/',views.pass_change2, name='pass_change2'),
    path('profile/', views.profile, name='profile'),
]
