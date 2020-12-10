from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Music, Category, Albums, Author
# Create your views here.


class MusicList(ListView):
    model = Music
    template_name = "templates/musics/music_list.html"
    context_object_name = "musics"


class MusicCategory(ListView):
    model = Category
    template_name = "templates/musics/"
    context_object_name = "categories"


class AlbumList(ListView):
    model = Albums
    template_name = "templates/musics/"
    context_object_name = "albums"


class AuthorList(ListView):
    model = Author
    template_name = "templates/musics/"
    context_object_name = "authors"


class MusicDetail(DetailView):
    model = Music
    template_name = "templates/musics/music_detail.html"
    context_object_name = "music"


