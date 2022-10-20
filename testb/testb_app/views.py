from django.shortcuts import render, redirect
from django.http import HttpResponse
from testb_app.models import *
from testb_app import forms
from django.db.models import Avg
# Create your views here.()


def Index(request):
    musician_list = Musician.objects.order_by('first_name')
    album_list = Album.objects.order_by('name')
    context = {'title': "Home Page",
               'musicians': musician_list, 'albums': album_list}
    return render(request, 'testb_app/index.html', context)


def Album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_info = Album.objects.filter(
        artist=artist_id).order_by('name', 'release_date')

    artist_rating = Album.objects.filter(
        artist=artist_id).aggregate(Avg('num_stars'))
    context = {'title': "List of Album Page",
               'artist': artist_info, 'album': album_info, 'avg_star': artist_rating}
    return render(request, 'testb_app/album_list.html', context)


def Musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'title': "Add Musician Page", 'musician_form': form}
    return render(request, 'testb_app/musician_form.html', context)


def Album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return Index(request)
    context = {'title': "Add Album Page", 'album_form': form}
    return render(request, 'testb_app/album_form.html', context)


def Edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save()
            return Album_list(request, artist_id)

    context = {'edit_form': form, 'artist': artist_info}
    return render(request, 'testb_app/edit_artist.html', context)


def Edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    context = {}
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)

        if form.is_valid():
            form.save()
            context.update({'success_text': 'Successfully Updated'})

    context.update({'edit_form': form, 'album': album_info})
    context.update({'album_id': album_id})
    # so it can be used to delete with the Primary Key (album_id) in edit_album.html
    return render(request, 'testb_app/edit_album.html', context)


def Delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    context = {'delete_msg': 'Album Deleted Successfully', 'album': album}
    return render(request, 'testb_app/delete.html', context)


def Delete_musician(request, artist_id):
    album = Musician.objects.get(pk=artist_id).delete()
    context = {'delete_msg': 'Album Deleted Successfully', 'album': album}
    return render(request, 'testb_app/delete.html', context)
