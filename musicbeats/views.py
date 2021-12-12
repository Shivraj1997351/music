from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from musicbeats.models import Song, Trendingsinger, Watchlater,History,Singer,FollowersCount, likesCount,Trendingsong
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth.hashers import make_password
from django.contrib.auth  import authenticate,  login, logout
from django.db.models import Q



def songs(request):
    song = Song.objects.all()
    return render(request,'musicbeats/songs.html',{'song':song})

def songpost(request,id):
    if request.user.is_authenticated:
        trend = Trendingsong.objects.filter(song_id=id).first()
        if trend:
           trend.count+=1
           trend.save()
        else:
            trends = Trendingsong.objects.create(song_id=id,count=1)
            trends.save()
        watch = Watchlater.objects.filter(Q(user=request.user) & Q(video_id=id)).exists()
        song = Song.objects.filter(song_id=id).first()
        likes = likesCount.objects.filter(liker=request.user.username,song_id=id).first()
        if likes:
            like_status = 'dislike'
        else:
            like_status = 'like'
        context = {'song':song,'watch':watch,'like_status':like_status}
    else:
        song = Song.objects.filter(song_id=id).first()
        context = {'song':song}
    return render(request,'musicbeats/songpost.html',context)

def signup(request):
 if request.method=="POST":
    username=request.POST['username']
    name=request.POST['name']
    pass1=request.POST['pass1']
    pass2=request.POST['pass2']
    uname = User.objects.filter(username=username)
    email = ''
    
    
    if uname:
        messages.warning(request, "Username should be unique")
        return redirect('signuppage')
    
    if len(username)<5:
        messages.warning(request, "User name length should be atleast 5")
        return redirect('signuppage')

    if not username.isalnum():
        messages.warning(request, "User name should only contain letters and numbers")
        return redirect('signuppage')
    
    if len(pass1)<8:
        messages.warning(request, "Password length should be atleast 8")
        return redirect('signuppage')
    
    if (pass1!= pass2):
        messages.warning(request, "Passwords do not match")
        return redirect('signuppage')
        
        
    myuser = User.objects.create_user(username,email,pass1)
    myuser.first_name= name
    myuser.save()
    messages.success(request, "Your account has been successfully created")
    return redirect('signuppage')
 return render(request,'musicbeats/signup.html')


def loginpage(request):
    if request.method=="POST":
        # Get the post parameters
        mloginusername=request.POST['loginusername']
        mloginpassword=request.POST['loginpassword']
        user=authenticate(username= mloginusername, password= mloginpassword)
        if user is not None:
            login(request, user)
            hashusername = make_password(mloginusername)
            hashpassword = make_password(mloginpassword)
            if 'next' in request.POST:
                response = redirect(request.POST.get('next'))
                response.set_cookie('mloginusername',hashusername,max_age=365 * 24 * 60 * 60)
                response.set_cookie('mloginpassword',hashpassword,max_age=365 * 24 * 60 * 60)
                return response 
            else:
                response = redirect('index')
                response.set_cookie('mloginusername',hashusername,max_age=365 * 24 * 60 * 60)
                response.set_cookie('mloginpassword',hashpassword,max_age=365 * 24 * 60 * 60)
                return response
        else:
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect("loginpage")

    return render(request,'musicbeats/loginpage.html')

def profile(request):
    lc = likesCount.objects.filter(liker=request.user)
    fc = FollowersCount.objects.filter(follower=request.user)
    ids = [] 
    for i in lc:
        ids.append(i.song_id)   
    song = Song.objects.filter(song_id__in=ids)
    ids1 = []
    for i in fc:
        ids1.append(i.singer)
    singer = Singer.objects.filter(singer__in=ids1)
    return render(request,'musicbeats/profile.html',{'song':song,'singer':singer})

def search(request):
    query = request.GET.get('query') 
    song = Song.objects.all()
    qs = song.filter(Q(name__icontains=query) | Q(singer__icontains=query) | Q(tags__icontains=query) | Q(movie__icontains=query))
    singer = Singer.objects.all()
    qs1 = singer.filter(singer__icontains=query)
    return render(request,'musicbeats/search.html',{'song':qs,'query':query,'singer':qs1})

def singers(request,singer):
    sing = Singer.objects.filter(singer=singer).first()  
    song = Song.objects.filter(singer=singer)
    trend = Trendingsinger.objects.filter(sing_id=sing.sing_id).first()
    if trend:
        trend.count+=1
        trend.save()
    else:
        trends = Trendingsinger.objects.create(sing_id=sing.sing_id,count=1)
        trends.save()
    if request.user.is_authenticated:
        user_followers = len(FollowersCount.objects.filter(singer=singer))
        user_followers0 = FollowersCount.objects.filter(singer=singer)
        user_followers1 = []
        for i in user_followers0:
            j = i.follower
            user_followers1.append(j)
        if request.user.username in user_followers1:
            follow_button_value = 'unfollow'          
        else:
            follow_button_value = 'follow'
        context = {'sing':sing,'song':song,'user_followers':user_followers,'follow_button_value':follow_button_value}
    else:
        user_followers = len(FollowersCount.objects.filter(singer=singer))
        context = {'sing':sing,'song':song,'user_followers':user_followers}
    return render(request,'musicbeats/singers.html',context)
    

          
def addwatchlater(request):
    if request.method == 'GET':
        video_id = request.GET['video_id']
        wl = Watchlater.objects.create(user=request.user,video_id=video_id)
        wl.save()
        data = {
            'message':'Added to queue'
        }
        return JsonResponse(data)

def watchlater(request):
    wl = Watchlater.objects.filter(user=request.user)
    ids = [] 
    for i in wl:
        ids.append(i.video_id)   
    song = Song.objects.filter(song_id__in=ids)
    return render(request,'musicbeats/watchlater.html',{'song':song})   

def removequeue(request):
    if request.method == 'GET':
     video_id = request.GET['video_id']
     wl = Watchlater.objects.get(video_id=video_id,user=request.user) 
     wl.delete()
     data = {
         'message':'Removed from queue'
     }
     return JsonResponse(data)

def removehistory(request):
    if request.method == 'GET':
     music_id = request.GET['music_id']
     ht = History.objects.get(music_id=music_id,user=request.user) 
     ht.delete()
     data = {
         'message':'Removed from history'
     }
     return JsonResponse(data)

def history(request):
    if request.method == 'POST':
        user = request.user
        music_id = request.POST['music_id']
        hist = History.objects.filter(user=user,music_id=music_id).first()
        if hist:
            hist.delete()
            history = History(user=user,music_id=music_id)
            history.save()
        else:
            history = History(user=user,music_id=music_id)
            history.save()
        return redirect(f'/musicbeats/songs/{music_id}')
    ht = History.objects.filter(user=request.user)
    ids = [] 
    for i in ht:
        ids.append(i.music_id)   
    song = Song.objects.filter(song_id__in=ids)
    return render(request,'musicbeats/history.html',{'song':song}) 


def handelLogout(request):
    logout(request)
    response = redirect('/')
    response.delete_cookie('mloginusername')
    response.delete_cookie('mloginpassword')
    return response