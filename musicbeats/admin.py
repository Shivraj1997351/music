from musicbeats.models import Song,Watchlater,History,Singer,FollowersCount,likesCount,Trendingsong,Trendingsinger,Playlist
from django.contrib import admin

# Register your models here.
admin.site.register((Song,Watchlater,History,Singer,FollowersCount,likesCount,Trendingsong,Trendingsinger,Playlist))