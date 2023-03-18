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