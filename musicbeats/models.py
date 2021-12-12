from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='songs')
    movie = models.CharField(max_length=100,default='NA')
    
    def __str__(self):
        return self.name
    

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    video_id = models.CharField(max_length=200000000)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    music_id = models.CharField(max_length=200000000)
    def __str__(self):
        return str(self.user)    

class Singer(models.Model):
    sing_id = models.AutoField(primary_key=True)
    singer = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return str(self.singer)
    
class FollowersCount(models.Model):
     follower_id = models.AutoField(primary_key=True)
     follower = models.CharField(max_length=100)
     singer = models.CharField(max_length=500)
     def __str__(self):
          return str(self.singer) 

class likesCount(models.Model):
    liker_id = models.AutoField(primary_key=True)   
    liker = models.CharField(max_length=100)
    song_id = models.CharField(max_length=200000000)
    def __str__(self):
        return str(self.song_id)
    
class Trendingsong(models.Model):
    trend_id = models.AutoField(primary_key=True)
    song_id = models.CharField(max_length=200000000)
    count = models.BigIntegerField()
    def __str__(self):
        return str(self.song_id)

class Trendingsinger(models.Model):
    trend_id = models.AutoField(primary_key=True)
    sing_id = models.CharField(max_length=2000)
    count = models.BigIntegerField()
    def __str__(self):
        return str(self.sing_id)

class Playlist(models.Model):
    play_id = models.AutoField(primary_key=True)
    song_id = models.ManyToManyField(Song,related_name='playlist')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='Anonymous')
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    