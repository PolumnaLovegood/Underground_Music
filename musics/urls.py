from django.urls import path
from .views import AuthorList, AlbumList, MusicList, AlbumMusicList

app_name = 'musics'

urlpatterns = [
    path("", AlbumList.as_view(), name="album_list"),
    path("authors/", AuthorList.as_view(), name="author_list"),
    path("musics/", MusicList.as_view(), name="music_list"),
    path("musics/<int:pk>/", AlbumMusicList.as_view(), name="album_music_list"),
]
