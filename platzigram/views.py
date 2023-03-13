from django.http import HttpResponse
from datetime import datetime 
import json 
def hello_wordl(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola, la hora actual del server es {now}'.format(now=now))

def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #import pdb; pdb.set_trace() #debuger
    data={
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted sucessfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='aplication/json')
def say_hi(request,name,age):
    if age<12:
        message='lo siento {}, no tienes la edad de estar aqui'.format(name)
    else:
        message='Bienvenido {}, Bienvenido a Platzigram'.format(name)
    return HttpResponse(message)
