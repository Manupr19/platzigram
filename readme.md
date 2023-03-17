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
creamos la app posts ```py manage.py startapp posts``` y en views.py de la aplicacionm post creamos el metodo list_posts
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

