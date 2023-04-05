from django.contrib import admin
from .models import Album, PlayList,Song, Style, SongList, Singer
# Register your models here.

admin.site.register(Album)
admin.site.register(PlayList)
admin.site.register(Song)
admin.site.register(Style)
admin.site.register(SongList)
admin.site.register(Singer)
