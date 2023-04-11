
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as post_views
from django.conf import settings
from users import views as user_views
def hello_world(request):
    return HttpResponse('Hello world')
urlpatterns = [
    
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('admin/',admin.site.urls),
    path('users/',include(('users.urls','users'),namespace='users')),

 
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
