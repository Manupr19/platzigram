from django.db import models
from django.contrib.auth.models import User
#class User(models.Model):
 #   email=models.EmailField(unique=True)
  #  password=models.CharField(max_length=100)
   # firts_name=models.CharField(max_length=100)
    #last_name=models.CharField(max_length=100)
    #is_admin=models.BooleanField(default=False)
    #bio=models.TextField(blank=True)
    #birthdate = models.DateField(blank=True,null=True)
    #created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now=True)

#def __str__(self):
 #   return self.email
class Post(models.Model):
 
 user=models.ForeignKey(User, on_delete=models.CASCADE)
 profile= models.ForeignKey('users.Profile', on_delete=models.CASCADE)

 title=models.CharField(max_length=255)
 photo= models.ImageField(upload_to='posts/photos')

 created= models.DateTimeField(auto_now=True)
 modified= models.DateTimeField(auto_now=True)

 def __str__(self):
  #devuelve titulo y username
  return '{} by @{}'.format(self.title,self.user.username)