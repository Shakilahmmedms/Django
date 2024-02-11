from django.urls import path,include
from .import views
urlpatterns = [
    path('about/',views.about),
    path('contact/',views.contact)
    # path('first_app/',include('first_app.urls'))
]
