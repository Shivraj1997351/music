from django.contrib import admin
from django.urls import path,include
from music import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('followers',views.followers),
    path('like',views.like),
    path('musicbeats/',include('musicbeats.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
