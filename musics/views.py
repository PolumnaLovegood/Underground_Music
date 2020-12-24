from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Music, Category, Albums, Author, Users
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


class MusicList(ListView):
    model = Music
    template_name = "musics/music_list.html"
    context_object_name = "musics"

    def get_queryset(self):
        return Music.objects.all()


class AlbumMusicList(ListView):
    model = Music
    template_name = "musics/album_music_list.html"
    context_object_name = "musics"

    def get_queryset(self):
        self.album = get_object_or_404(Albums, pk=self.kwargs['pk'])
        return Music.objects.filter(album=self.album)


class MusicCategory(ListView):
    model = Category
    template_name = "templates/musics/"
    context_object_name = "categories"


class AlbumList(ListView):
    model = Albums
    template_name = "musics/album_list.html"
    context_object_name = "albums"

    def get_queryset(self):
        return Albums.objects.all()


class AuthorList(ListView):
    model = Author
    template_name = "musics/author_list.html"
    context_object_name = "authors"

    def get_queryset(self):
        return Author.objects.all()


class AuthorAlbumList(ListView):
    model = Albums
    template_name = "musics/authors_albums.html"
    context_object_name = "authors_albums"

    def get_queryset(self):
        self.author = get_object_or_404(Author, pk=self.kwargs['pk'])
        return Albums.objects.filter(author=self.author)


class MusicCreate(LoginRequiredMixin, CreateView):
    model = Music
    fields = ["name", "music", "author", "album", "category", "position"]
    success_url = reverse_lazy("musics:music_list")


class MusicDetail(DetailView):
    model = Music
    template_name = "musics/music_detail.html"
    context_object_name = "music"


@login_required
def favourite_song(request, pk):
    song = get_object_or_404(Music, pk=pk)
    user, created = Users.objects.get_or_create(user=request.user)
    music = Music.objects.get(name=song)
    if not user.favorite_music.filter(music=song).exists():
        user.favorite_music.add(music)
        user.save()
        print(str(user.favorite_music))
        print(str(song))
        return redirect('musics:favorite_list')
    else:
        messages.info(request, 'Этот трек уже в ваших избранных!')
        return redirect('musics:favorite_list')


class FavoriteMusic(ListView):
    model = Users
    template_name = "musics/favorite_songs.html"
    context_object_name = "favorite_list"

    def get_queryset(self):
        return Users.objects.get(user=self.request.user)
