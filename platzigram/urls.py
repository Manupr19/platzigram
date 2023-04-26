
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as post_views
from django.conf import settings
from users import views as user_views
from users import models
from django.shortcuts import render
from django.contrib.auth.models import User


def hello_world(request):
    return HttpResponse('Hello world')

def guardarfoto(request):
    print("guardando foto")
    if request.method == 'POST':
        p=models.Fotos()
        p.img=request.FILES["photo"]
        p.user= User.objects.get(id = 1) 
        p.save()
        
    return HttpResponse('Hello world')

def vercamara(request):
    return render(request,"camara.html",{})

urlpatterns = [
    
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('admin/',admin.site.urls),
    path('users/',include(('users.urls','users'), namespace='users')),
    path('hola/',hello_world),
    path('guardarfoto/',guardarfoto),
    path('vercamara/',vercamara),

 
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
