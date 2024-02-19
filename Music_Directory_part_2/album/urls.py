from django.urls import path
from .import views

urlpatterns = [
    # path('create/', views.creat_album, name='create_album'),
    path('create/', views.CreateAlbumView.as_view(), name='create_album'),
    # path('edit/<int:id>', views.edit_album, name='edit_album'),
    path('edit/<int:id>', views.EditAlbumView.as_view(), name='edit_album'),
    # path('delete/<int:id>', views.delete_album, name='delete_album'),
    path('delete/<int:id>', views.DeleteAlbumView.as_view(), name='delete_album'),
]
