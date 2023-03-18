
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as post_views

def hello_world(request):
    return HttpResponse('Hello world')
urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello-world/',local_views.hello_wordl),
    path('sorted/',local_views.sort_integers),
    path('hi/<str:name>/<int:age>/',local_views.say_hi),
    path('posts/', post_views.list_posts),
]
