from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# Exception
from django.db.utils import IntegrityError
from django.urls import reverse
from posts.models import Post
# Models
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.models import User

# forms
from users.forms import Profile, SignupForm

from django.views.generic import DetailView,FormView
from django.urls import reverse_lazy
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

class loginView(auth_views.LoginView):
   template_name='users/login.html'

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
   
 print('haciendo login')
 return render(request,'users/login.html')

@login_required
def logout_view(request):
   logout(request)
   return redirect('users:login')

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

     
@login_required
def update_profile(request):
    profile=request.user.profile
    if request.method == 'POST':
        form = Profile(request.POST,request.FILES)
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
        form= Profile()

    return render(
        request=request,template_name='users/update_profile.html',
        context={
        'profile':profile,
        'user':request.user,
        'form': form,
        })
