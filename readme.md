##platzigram
#views
#EL OBJECTO REQUEST
lo primero que usamos es la libreria datetime para loas dias horas y minutos y definimos un metodo para ello 

```
from datetime import datetime 
def hello_wordl(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola, la hora actual del server es {now}'.format(now=now))
```
despues creamos un metodo "hi" dentro de el utilizamos el debugger con:

```import pdb; pdb.set_trace()```

Por ultimo pasamos por la url del navegador y los mostramos en principio

``` numbers = request.GET['numbers']
    return HttpResponse(str(numbers))
```
## PASANDO ARGUMENTOS POR URL 
Cuando se nos pide que mostremos los numeros ordenados lo que debemos hacer es hacer una lista de numeros enteros y ordenar con la funcion sorted (lista_numeros)

``` 
    numbers = [int(i) for i in request.GET['numbers']]
    sorted_ints = sorted(numbers)
    import pdb; pdb.set_trace() #debuger
    return HttpResponse(str(numbers))

```
si queremos responder con un json lo que hacemos primero es importar la libreria "json", tambien podemos añadir un diccionario y tendriamos que usar el metodo json.dump(diccionario) para que funcione, la variable indent son los espacios que queremos dejar

Creamos el path path('hi/<str:name>/<int:age>/',views.say_hi), de esta forma le pasamos dos parametros en la url cuando ponemos hi y despues accedemos al método say_hi el cual deniega la entrada a quien sea menor que 12 años
```
def say_hi(request,name,age):
    if age<12:
        message='lo siento {}, no tienes la edad de estar aqui'.format(name)
    else:
        message='Bienvenido {}, Bienvenido a Platzigram'.format(name)
    return HttpResponse(message)

```

## Creacion de la primera app
creamos la app posts ```py manage.py startapp posts``` y en views.py de la aplicacion post creamos el metodo list_posts
```
def list_posts(request):
    posts=[1,2,3]
    return HttpResponse(str(posts))
```
no olvidar importar libreria from django.http import HttpResponse

Una buena practica en las urls es poner nombre a las locales y a las urls de la las apps (local_views/post_views)

### Listar posts

La siguiente actividad consistia en listar los diferentes posts, sin usar aun la base de datos de tal forma que estos usuarios estarían guardados en una variable posts que guardaria todo sus atributos, este es un ejemplo:

´´´
posts = [
{
    'name':'Daniel Lopez',
    'user':'danilp',
    'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture':'https://pbs.twimg.com/media/FJDsHEtWYAAFR7f.jpg',

},
]
```
después crearemos el metodo list_posts(request) que lo que hara es listar estos haciendo un bucle para listar todos y por último daremos una respuesta con httpResponse( no olvidar el .join(content))
```
def list_posts(request):
    content = []
    for post in posts:
        content.append(""" 
        <p><strong>{name}</strong></p>
        <p><small>{user} -<i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    
    return HttpResponse('<br>'.join(content))

```

## Introduccion al template system

lo primero que haremos sera crear la carpeta templates en posts, y dentro crear un archivo feed.html con un hola mundo, posteriormente nos vamos a views quitamos la libreria 
httpResponse y añadimos:

```from django.shortcuts import render```

despues modificamos el metodo list_posts(request) de tal forma que quede asi:
```
def list_posts(request):
   
    return render(request,'feed.html')

```
Fíjate en que no ponemos la ruta hasta feed, ya que en settings esta definido que busque en las carpetas llamadas templates por eso no es necesario

Podemos tambien pasarle al cuestionario parametros pro ejemplo mi nombre, despues en el documento html solo tendriamos que poner {{name}} para verlo 

```
def list_posts(request):
   
    return render(request,'feed.html',{'name':'Manu'})
```
Ahora mostraremos los posts pasandole una variable llamada posts que coge los datos definidos arriba
```
def list_posts(request):
   
    return render(request,'feed.html',{'posts':posts})
```
A continuación le añadimos un poco de complejidad a los posts añadiendole mas atributos
```
posts = [
{
    'title':'Usuario 1',
    'user': {
        'name':'Daniel Lopez',
        'picture':'https://pbs.twimg.com/media/FJDsHEtWYAAFR7f.jpg',
    },
    'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo':'xxx',

},
]
```
y en feed.html cambiamos a
´´´
{% for post in posts %}
<p>{{post.title}}</p>
{% endfor %}
```
De esta forma veremos los titulos en parrafos distintos

seguimos cambiando el documento html (atajo "!" para tener una sintaxis html completa)

Posteriormente en feed.html con ayuda de boostrap hacemos una plantilla en la que haremos una especie de vista de instagram

´´´
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Platzigram</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
</head>
<body>
    <br>
    <div class="container">
        <div class="row">
            {% for post in posts %}
            <div class="col-lg-4 offset-lg-4"></div>
            <div class="media">
                <img class="mr-3 rounded-circle" src="{{ post.user.picture }}" alt="{{ post.user.name }}">
                <div class="media-body">
                    <h5 class="mt-0">{{ post.user.name }}</h5>
                    {{ post.timestamp }}
                </div>
            </div>

           <img class="img-fluid mt-3 border rounded" src="{{post.photo}}" alt="{{post.title}}">
           <h6 class="ml-1 mt-1">{{ post.title }}</h6>
        </div>
        {% endfor %}
    </div>
</body>
</html>
```
## Patrones de diseño y Django

Vemos el MVC:

Controler- maneja la logica y el request sabe que hacer en ese momento y sabe que template tiene que mostrar, el controler va a cambiar los datos a traves del modelo

Modelo- se encarga de definir la estructura de los datos, el acceso a ellos e incluso la validación 

Vista- Se encarga de como presentar esos datos que alfinal van a ser mostrados al usuario 

vemos el MTV(model template view) implementado por Django:

Modelo- Define la estructura de los datos

Template-Logica de presentacion de datos

Views- Encargado de traer los datos y pasarlos al template
# MODELOS
## La M en el MTV
Quitamos error de migraciones con ```py manage.py migrate```
creamos en models.py una clase usuario con todos los campo
```
from django.db import models

class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    firts_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    bio=models.TextField(blank=True)
    birthdate = models.DateField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
```
utilizamos el comando ```py manage.py makemigrations```
y debemos hacer py manage.py migrate para solucionar el warning de la migracion post

NOTA:
-Makemigrations- Va a buscar los cambios en los modelos y lo va a reflejar en el archivo initial
-migrate- Va a aplicar esos cambios en la base de datos

## El ORM de Django

Una vez tenemos el modelo lo que sigue es crear datos usando el ORM 

para usar el shell con nuestra app usamos ```py manage.py shell```
creamos un usuario desde aqui con los siguientes atributos
```
Manu = User.objects.create(
... email='hola@gmail.com',       
... password='1234567',     
... firts_name='Manu',  
... last_name='Pazos'             
... )
```
Otra manera desde la shell

```
Arturo = User()
>>> Arturo.email='arturo@gmail.com'
>>> Arturo.firts_name = 'Arturo'
>>> Arturo.last_name='Carmona' 
>>> Arturo.password='1234'     
>>> Arturo.is_admin = True
>>> Arturo.save()
```
Si queremos borrarlo solo tenemos que hacer >>>Usuario.delete()

Para traer usuarios:
 <<< from posts.models import User
 <<< user = User.objects.get(email='freddier@platzi.com')
 
 A partir de aqui podemos ver todos los atributos de ese user, ejemplo user.password 

 <<< platzi_users = User.objects.filter(email__endwith='@gmail.com')

User.object.all() para traer todos

Tener en cuenta que get solo regresa un objeto 

## Extendiendo el modelo de usuario 

Desde la shell creamos un nuevo usuario, primero ponemos como vimos antes ```py manage.py shell```;

A continuación importamos la libreria siguiente y creamos un nuevo usuario:
```
from django.contrib.auth.models import User 
u= User.objects.create_user(username='yesika',password='admin123') 

```
Posteriormente podemos comprobar los datos de este usuario poniendo u.pk o u.password y nos fijaremos que la contraseña esta encriptada.

Ahora creamos un superusuario:
```py manage.py createsuperuser ```

Tambien debemos importar en urls.py la libreria
```from django.contrib import admin```

Y añadir ``` path('admin/',admin.site.urls),```

## Implementación del modelo de usuarios

Creamos una nueva app para usuarios ```py manage.py startapp users```

Posteriormente vamos a models.py de la app y vamos creando los atributos( user, website, phone number), dentro de la clase profile:
NOTA:cada user es unico por ello la relacion ONETOONE
```
class Profile(models.Mode):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website=models.URLField(max_length=200,blank=True)
    phone_number=models.CharField(max_length=20,blank=True)

    picture=models.ImageField(upload_to='users/pictures',blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.user.username
```
despues instalamos pillow, hacemos make migrations y migrate

y vemos como se ha creado la tabla users_profile en la base de datos

## Explorando el dashboard de administración 

Añadimos funcionalidades de admin en admin.py importando libreria 
```
from users.models import Profile
admin.site.register(Profile)

```
Esto desbloquea una opcion en la pantalla de admin para gestionar estos

Posteriormente creamos una clase para mostrar todo los campos de Profile
```
@admin.register(Profile) #se llama decorador para hacerlo en una linea
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','phone_number','website','picture')
```
añadimos list_display_links para ir al detalle de cada uno 

```list_display_links=('pk','user','phone_number')```

Podemos usar list_editable para editar los datos desde la página, NOTA: solo puede estar o en list_display_links o en list_editable

```  list_editable=('phone_number','website','picture')```

Despues en los admin como puede haber mas de uno añadimos la función de buscar para ello creamos otra variable search_fields:

```
search_fields = ('user__email','user__firtsname','user_last_name','phone_number')

```
Por último añadiremos filtros para una mejor busqueda

```
list_filter=('created','modified','user__is_active','user__is_staff')

```
## Dashboard de administración 
 Seguimos añadiendo cosas a admin.py, primero añadiremos las librerias

  ```
from users.models import Profile
from django.contrib.auth.models import User
```
Después creamos los metodos ProfileInline y userAdmin
```
class ProfileInline(admin.StackedInline):
        model = Profile
        can_delete = False
        verbose_name_plural='profiles'

    class UserAdmin(BaseUseradmin):
        #añadir profile admin to base user admin
        #inlines=(ProfileInline,)
        list_display=(
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',

        )

    admin.site.unregister(User)
    admin.site.register(User,UserAdmin)
```
NOTA: Preguntar porque hay un error en Useradmin si la clase esta justo arriba, tampoco va en urls py lo de las imagenes
## Creacion del modelo de posts 

Lo siguiente que hacemos es modificar la clase Post en model.py de users 
´´´
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
  ```
  Después para solucionar el problema de que las imagenes en admin no se ven en el url pattern haremos lo siguiente:
  
  primero importar las librerias from django.conf.urls.static import static y from django.conf import settings
  y al final de urlpatterns hacer :

  ```
urlpatterns = [
    path('admin/',admin.site.urls),
    path('hello-world/',local_views.hello_wordl),
    path('sorted/',local_views.sort_integers),
    path('hi/<str:name>/<int:age>/',local_views.say_hi),
    path('posts/', post_views.list_posts),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

  ```
  Por último en settings añadiremos 

  ```

  MEDIA_ROOT=BASE_DIR / 'media'
  MEDIA_URL='/media/'

  ```

## Templates y archivos estaticos

En este apartado hemos creado los templates css, hemos añadido imagenes y creado todos los documentos html ademas de hacer el nav que es la pantalla de posts inicial

NOTA: PREGUNTAR PORQUE NO SALE LOS ICONOS DE ARRIBA SOLO EL DE INSTAGRAM

## Login

Vamos a realizr el proceso de autenticación 
para ello primero creamos el path 

``` path('user/login/',user_views.login_view,name='login')```

despues nos vamos a views y crearemos la funcion login_views

``` from django.contrib.auth import authenticate, login 
from django.shortcuts import render

def login_view(request):
    return render(request,'users/login.html')
```
NOTA: Siempre que necesite un debuger utilizar  import pdb; pdb.set_trace()

Ahora nos vamos a /templates/users/login.html lo que haremos sera hacer un formulario y poner el token csrf
```
{% extends "users/base.html" %}



{% block head_content %}
<title>Platzigram sign in</title>
{% endblock%}

{% block container %}

   <form method="POST" action ="{% url "login" %}">
      {% csrf_token %}
    
      <input type="text" placeholder="Username" name="username" />
      <input type="password" placeholder="Password" name="password" />
      <button type="submit">Inicia sesion!</button>
   </form>
{% endblock %}

```
posteriormente hacemos en views.py el trato con el inicio de sesión correcto e incorrecto
```
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
 ```
 Posteriormente en login.html cuando el login sea incorrecto lo pondremos en rojo de esta form 

 ```
    {% if error %}
      <p style="color:red;">{{error}}</p>
   {% endif %}

```
Seria conveniente proteger la vista de post para que no entraran poniendo la url sin estar logeados para ello
nos vamos a la vista de post y utilizando la libreria from django.contrib.auth.decorators import login_required, la utilizamos asi:

``` 
@login_required
def list_posts(request):
   
    return render(request,'posts/feed.html',{'posts':posts})

```
NOTA: PREGUNTAR PORQUE NO LO PROTEGE 

## Logout

Lo primero que debemos hacer es dirigirnos a urls.py y crear un path para el logout, despues crearemos la vista asociada a este path:
```path('accounts/logout/',user_views.logout_view,name='logout'),```

Después creamos el metodo y le ponemos @loginrequiered con la libreria from django.contrib.auth.decorators import login_required, para que no se pueda acceder a el directamente como pasaba anteriormente con posts

```
@login_required
def logout_view(request):
   logout(request)
   return redirect('login')

```

## Registro de usuario 

lo primero que hacemos es crear el path en urls.py 
```path('accounts/signup/',user_views.signup,name='signup'),```
en views creamos el metodo signup 
```
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
   ``` 
   Por ultimo creamos el formulario de signup 
   ´´´
   {% extends "users/base.html" %}

{% block head_content %}
<title> Platzigram signup</title>
{% endblock %}

{% block container %}
    {% if error %}
        <p class="alert alert-danger"></p>
    {% endif %}
    <form action="{% url 'signup' %}" method="POST">
        {% csrf_token %}

        <div class="form-group">
            <input class="form-control" type="text" placeholder="Username" name="username" required="true"/>
        </div>
        <div class="form-group">
            <input class="form-control" type="password" placeholder="Password" name="password" required="true"/>
        </div>
        <div class="form-group">
            <input class="form-control" type="password" placeholder="Password confirmation" name="password_confirmation" required="true"/>
        </div>
        <div class="form-group">
            <input class="form-control" type="text" placeholder="Firts name" name="firts_name" required="true"/>
        </div>
        <div class="form-group">
            <input class="form-control" type="text" placeholder="Last name" name="last_name" required="true"/>
        </div>
        <div class="form-group">
            <input class="form-control" type="email" placeholder="Email address" name="email" required="true"/>
        </div>
        <button class="btn btn-primary btn-block mt-5" type="'submit">Registrate!</button>
    </form>
{% endblock %}
```

## Midleware

Modificación de objetos antes y despues de salir de la vista
- Lo primero es ir a las urls y crear una vista llamada accounts/me/profile
-despues vamos a /users/views y creamos dicha funcion:

```
def update_profile(request):
return render(request,'users/update_profile.html')
```
Como vemos invoca a update_profile.html lo que haremos a continuacion es formar este documento

```
{% extends "base.html" %}

{% block head_content %}
<title>@{{request.user.username}} | Update profile</title>
{% endblock %}

{% block container %}
    <h1 class="mt-5">@{{request.user.username}}</h1>
{% endblock %}
```
posteriormente creamos midleware.py

```
from django.shortcuts import redirect

class ProfileCompletionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                return redirect('update_profile')
        response = self.get_response(request)
        return response
```
Posteriormente vamos a settings.py y instalamos nuestro midleware

y este estara funcionando para perfiles que no esten completos los redireccionara a accounts/me/update

## Formularios en django

Actualizamos el metodo update_profile
```
def update_profile(request):
    profile= request.user.profile

    return render(request=request,template_name='users/update_profile.html',context={'profile':profile,'user':request.user})

```
despues modificamos el update_profile

django form fields reference (documentacion)

creamos forms.py y dentro añadimos una clase ProfileForm
```
from django import forms

class ProfileForm(forms.Form):
    website=forms.URLField(max_length=200,required=True)
    biography= forms.CharField(max_length=500,required=False)
    phone_number= forms.CharField(max_length=20,required=False)
    picture=forms.ImageField()
    
```
Dentro del formulario update_profile deberemos retocar ciertas cosas, por ejemplo añadir si hay un error en el formulario que me notifique cual es 
```
{% if form.errors %}
                    <p class="alert alert-danger">{{form.
                errors}}</p>
                {% endif %}
```
Nota: tambien debemos cambiar ``` <form action="{% url 'update_profile' %}" method="POST" enctype="multipart/form-data">``` para que se puedan subir archivos y cambiar en las vistas ```form = ProfileForm(request.POST,request.FILES)```

Despues procederemos a guardar los datos
```
 if form.is_valid():
            data= form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
      
            profile.picture = data['picture']
            profile.save()
```
por ultimo hacemos return redirect('update_profile') a la misma pagina y mostramos la imagen de esta forma:
```
   {% if profile.picture %}
                        <img src="{{ profile.picture.url }}" class="rounded-circle" height="50" />
                    {% else%}
                        <img src="{% static 'img/default-profile.png' %}" class="rounded-circle" height="50" />
                    {% endif %}
```
NOTA: al recargar no volvemos a mandar el formulario por el redirect

## Mostrando el Form en el template
 Lo que haremos es mejorar la forma de mostrar los errores 
 ```class="form-control {% if form.website.errors %}is-invalid{% endif %}"```
 ```  value="{% if form.errors %}{{ form.website.value }}{% else %}{{ profile.website }}{% endif %}
 ``` 
 despues le decimos cual fue el error

 ```
 <div class="invalid-feedback">
                        {% for error in form.website.errors %}
                            {{ error }}
                        {% endfor%}
                    </div>
                </div>
```
```
   {% for error in form.picture.errors %}
                <div class="alert alert-danger">
                    <b>Picture: </b>{{ error }}
                </div>
                {% endfor %}


```
esto lo aplicamos en todos los campos, biography y igual con phone_number
```
## Model forms
Otra manera de creacion de forms
lo primero que hacemos es crear un path nuevo para la creacion de nuevos posts en urls.py 
```
path('posts/new',post_views.create_post,name='create_post'),
```
y despues creamos el metodo en views.py de post
```
@login_required
def create_posts(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form= PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
       
    )
```
y creamos posts.forms.py

```

# Django
from django import forms

# Models
from posts.models import Post


class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
``` 
Despues creamos en los templates new.html
```
{% extends "base.html" %}

{% block head_content %}
<title>Create new post</title>
{% endblock %}

{% block container %}

    <div class="container">
        <div class="row justify-content-md-center">
            <div class="col-6 pt-3 pb-3" id="profile-box">
                <h4 class="mb-4">Post a new photo!</h4>

                <form method="POST" enctype="multipart/form-data">
                    {% csrf_token %}

                    <input type="hidden" name="user" value="{{ user.pk}}" />
                    <input type="hidden" name="profile" value="{{ profile.pk }}" />

                    {# Website field #}
                    <div class="form-group">
                        <input
                            class="form-control {% if form.title.errors %}is-invalid{% endif %}"
                            type="text"
                            name="title"
                            placeholder="Title"
                        >
                        <div class="invalid-feedback">
                            {% for error in form.title.errors %}{{ error }}{% endfor %}
                        </div>
                    </div>

                    {# Photo field #}
                    <div class="form-group">
                        <label>Choose your photo:</label>
                        <input
                            class="form-control {% if form.photo.errors %}is-invalid{% endif %}"
                            type="file"
                            name="photo"
                            placeholder="photo"
                        >
                        <div class="invalid-feedback">
                            {% for error in form.photo.errors %}{{ error }}{% endfor %}
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary btn-block mt-5">Publish!</button>
                </form>
            </div>
        </div>
    </div>

{% endblock %}
```
