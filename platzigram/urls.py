
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as post_views
from django.conf import settings
from users import views as user_views
def hello_world(request):
    return HttpResponse('Hello world')
urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello-world/',local_views.hello_world, name='hello_world'),
    path('sorted/',local_views.sort_integers,name='sort'),
    path('hi/<str:name>/<int:age>/',local_views.say_hi,name='hi'),
    path('posts/', post_views.list_posts,name='feed'),
    path('accounts/login/',user_views.login_view,name='login'),
    path('accounts/logout/',user_views.logout_view,name='logout'),
    path('accounts/signup/',user_views.signup,name='signup'),
    path('accounts/me/profile',user_views.update_profile,name='update_profile'),
    path('posts/new',post_views.create_posts,name='create_post'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
