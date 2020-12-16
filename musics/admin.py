from django.contrib import admin
from .models import Author, Albums, Music, Category

admin.site.register(Author)
admin.site.register(Albums)
admin.site.register(Music)
admin.site.register(Category)

