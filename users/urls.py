from django.urls import path 
from django.views.generic import TemplateView
from users import views

urlpatterns=[
      path(route='<str:username>/',view=TemplateView.as_view(template_name='users/detail'),name='detail'),
    path(route='accounts/login/', view=views.login_view, name='login'),
    path(route='accounts/logout/', view=views.logout_view, name='logout'),
    path(route='accounts/signup/', view=views.signup, name='signup'),
    path(route='accounts/me/profile', view=views.update_profile, name='update_profile'),
]