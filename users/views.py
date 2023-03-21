from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
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
      username= request.POST['username']
      passwd = request.POST['password']
      passwd_con = request.POST['password_confirmation']
      if passwd!=passwd_con:
         return render(request,'users/signup.html', {'error': 'Confirmacion de contraseña no coincide'})
      try:
            user= User.objects.create_user(username=username,password=passwd)
      except IntegrityError:
            return render(request,'users/signup.html', {'error': 'el nombre de usuario esta ya en uso'})
      user.firts_name = request.POST['firts_name']
      user.last_name = request.POST['last_name']
      user.email = request.POST['email']
      user.save()
      profile= Profile(user=user)
      profile.save()

      return redirect('login')
   return render(request,'users/signup.html')