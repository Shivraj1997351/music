from django.urls import path
from . import views
urlpatterns = [
    path('songs',views.songs,name='songs'), 
    path('songs/<int:id>',views.songpost,name='songpost'),
    path('removequeue',views.removequeue),
    path('removehistory',views.removehistory),
    path('profile',views.profile,name='profile'),
    path('watchlater',views.watchlater,name="watchlater"),
    path('history',views.history,name='history'),
    path('addwatchlater',views.addwatchlater),
    path('search',views.search,name='search'),
    path('singers/<str:singer>',views.singers,name='singers'),
    path('signuppage',views.signup,name="signuppage"),
    path('loginpage',views.loginpage,name="loginpage"),   
    path('logout', views.handelLogout, name="handleLogout"), 
] 
