from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Music, Category, Albums, Author
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


class MusicDetail(DetailView):
    model = Music
    template_name = "musics/music_detail.html"
    context_object_name = "music"


