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
##PASANDO ARGUMENTOS POR URL 
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

##creacion de la primera app
creamos la app posts ```py manage.py startapp posts``` y en views.py de la aplicacionm post creamos el metodo list_posts
```
def list_posts(request):
    posts=[1,2,3]
    return HttpResponse(str(posts))
```
no olvidar importar libreria from django.http import HttpResponse

Una buena practica en las urls es poner nombre a las locales y a las urls de la las apps (local_views/post_views)