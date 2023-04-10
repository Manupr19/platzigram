from django import forms

from django.contrib.auth.models import User
from users.models import Profile
class SignupForm(forms.Form):
    username = forms.CharField(min_length=4,max_length=50)
    password = forms.CharField(max_length=70,widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70,widget=forms.PasswordInput())

    firts_name = forms.CharField(min_length=2,max_length=50)
    last_name= forms.CharField(min_length=2,max_length=50)

    email=forms.CharField(min_length=6,max_length=70,widget=forms.EmailInput())

    def clean_username(self):
        username= self.cleaned_data['username'].exist()
        username_taken= User.objects.filter(username=username)
        if username_taken:
            raise forms.ValidationError('Username en uso ')
        return username
    def clean(self):
        data = super().clean()
        password = data['password']
        passwordconf = data['password_confirmation']

        if password != passwordconf:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return data
    def safe(self):
        data= self.cleaned_data
        data.pop('password_confirmation') #es un dato que no nos sirve de nada por eso lo saco asi

        user = user.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
        
class ProfileForm(forms.Form):
    website=forms.URLField(max_length=200,required=True)
    biography= forms.CharField(max_length=500,required=False)
    phone_number= forms.CharField(max_length=20,required=False)
    picture=forms.ImageField()
    