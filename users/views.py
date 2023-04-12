from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Exception
from django.db.utils import IntegrityError
from django.urls import reverse
from posts.models import Post
# Models
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.models import User

# forms
from users.forms import ProfileForm, SignupForm

from django.views.generic import DetailView
class UserDetailView(LoginRequiredMixin,DetailView):
   template_name= 'users/detail.html'
   slug_field ='username'
   slug_url_kwarg = 'username'
   queryset = User.objects.all()
   context_object_name = 'user'

   def get_context_data(self,**kwargs):
      context=super().get_context_data(**kwargs)
      user= self.get_object()
      context['posts']= Post.objects.filter(user=user).order_by('-created')
      return context



def login_view(request):
 if request.method == 'POST':
    username = request.POST['username']
    password=request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request,user)
        return redirect('posts:feed')
    else:
        return render(request,'users/login.html', {'error':'Contraseña o usuario no valido'})
   
 
 return render(request,'users/login.html')

#@login_required
def logout_view(request):
   logout(request)
   return redirect('login')

def signup(request):
   if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('users:login')
      else:
         form = SignupForm()
      return render(
         request=request,
         template_name='users/signup.html',
         context={'form' :form}
      )

     
#@login_required
def update_profile(request):
    profile=request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data= form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form= ProfileForm()

    return render(
        request=request,template_name='users/update_profile.html',
        context={
        'profile':profile,
        'user':request.user,
        'form': form,
        })
