from django.urls import path
from django.conf.urls import url
from .views import AuthorList, AlbumList, MusicList, AlbumMusicList, MusicCreate, FavoriteMusic, favourite_song

app_name = 'musics'

urlpatterns = [
    path("", AlbumList.as_view(), name="album_list"),
    path("authors/", AuthorList.as_view(), name="author_list"),
    path("musics/", MusicList.as_view(), name="music_list"),
    path("musics/<int:pk>/", AlbumMusicList.as_view(), name="album_music_list"),
    path("new/", MusicCreate.as_view(), name="music_form"),
    path("favorite_list/", FavoriteMusic.as_view(), name="favorite_list"),
    path("like/<int:pk>/", favourite_song, name="like_song"),
]
