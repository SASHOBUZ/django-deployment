from django.urls import re_path as url
from django.urls import path
from testb_app import views

app_name = "testb_app"

urlpatterns = [

    path('', views.Index, name='index'),
    path('add_album/', views.Album_form, name="album_form"),
    path('add_musician/', views.Musician_form, name='musician_form'),
    path('album_list/<int:artist_id>/', views.Album_list, name='album_list'),
    path('edit_artist/<int:artist_id>/', views.Edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.Edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/',
         views.Delete_album, name='delete_album'),
    path('delete_musician/<int:artist_id>/',
         views.Delete_musician, name='delete_musician'),
]
