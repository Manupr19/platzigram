from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Exception
from django.db.utils import IntegrityError
# Models
from django.contrib.auth.models import User
from users.models import Profile
# forms
from users.forms import ProfileForm, SignupForm

def login_view(request):
 if request.method == 'POST':
    username = request.POST['username']
    password=request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request,user)
        return redirect('feed')
    else:
        return render(request,'users/login.html', {'error':'Contraseña o usuario no valido'})
   
 
 return render(request,'users/login.html')

@login_required
def logout_view(request):
   logout(request)
   return redirect('login')

def signup(request):
   if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('login')
      else:
         form = SignupForm()
      return render(
         request=request,
         template_name='users/signup.html',
         context={'form' :form}
      )

     
@login_required
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

            return redirect('update_profile')
    else:
        form= ProfileForm()

    return render(
        request=request,template_name='users/update_profile.html',
        context={
        'profile':profile,
        'user':request.user,
        'form': form,
        })
