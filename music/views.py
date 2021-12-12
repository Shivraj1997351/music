from django.shortcuts import redirect, render 
from musicbeats.models import History, Playlist, Singer, Song,FollowersCount,likesCount,Trendingsong,Trendingsinger
from django.http.response import JsonResponse
def index(request):
    trend = Trendingsong.objects.filter(count__gt=3)
    ids1 = []
    for i in trend:
        ids1.append(i.song_id)
    song = Song.objects.filter(song_id__in=ids1)
    
    Trendingsing = Trendingsinger.objects.filter(count__gt=3)
    ids2 = []
    for i in Trendingsing:
        ids2.append(i.sing_id)
    trendsing = Singer.objects.filter(sing_id__in=ids2)
    
    fav = FollowersCount.objects.filter(follower=request.user)
    ids = [] 
    for i in fav:
        ids.append(i.singer)   
    favourite = Song.objects.filter(singer__in=ids)
    return render(request,'musicbeats/index.html',{'song':song,'favourite':favourite,'trendsing':trendsing})

def followers(request):
    if request.method == 'GET':
        follower = request.user.username  
        singer = request.GET['value']
        value = FollowersCount.objects.filter(follower=follower,singer=singer).first()
        if value:
            followers_cnt = FollowersCount.objects.get(follower=follower,singer=singer)
            followers_cnt.delete()
            fmsg = 'Follow'
            fcount = len(FollowersCount.objects.filter(singer=singer))
            data = {
                'fmsg':fmsg,
                'fcount':fcount
            }


        else:
            followers_cnt = FollowersCount.objects.create(follower=follower,singer=singer)
            followers_cnt.save()
            fmsg = 'UnFollow'
            fcount = len(FollowersCount.objects.filter(singer=singer))
            data = {
                'fmsg':fmsg,
                'fcount':fcount
            }
            
        return JsonResponse(data)


def like(request):
    if request.method == 'GET':
        liker = request.user.username  
        song_id = request.GET['value']
        value = likesCount.objects.filter(liker=liker,song_id=song_id).first()
        if value:
            like_cnt = likesCount.objects.get(liker=liker,song_id=song_id)
            like_cnt.delete()
            data = {
                'fmsg':'far fa-heart',
                'css':'black',
                'message':'Removed from favourites'
            }
        else:
            like_cnt = likesCount.objects.create(liker=liker,song_id=song_id)
            like_cnt.save()
            data = {
                'fmsg':'fas fa-heart',
                'css':'red',
                'message':'Added to favourites'
            }
            
        return JsonResponse(data)

    