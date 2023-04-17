from django.urls import path 
from django.views.generic import TemplateView
from users import views
from django.http import HttpResponse

def login_view(request):
    return HttpResponse('Hello world')

urlpatterns=[
    
    
    path(route='login/', view=views.login_view, name='login'),
    path(route='logout/', view=views.logout_view, name='logout'),
    path(route='signup/', view=views.signup, name='signup'),
    path(route='me/profile', view=views.update_profile, name='update'),
    path(route='<str:username>/',view=views.UserDetailView.as_view(),name='detail'),
]