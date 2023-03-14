from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
{
    'name':'Daniel Lopez',
    'user':'danilp',
    'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture':'https://cflvdg.avoz.es/sc/wWrf3TUzQyWKEFzZTo3imnw4rr4=/480x/2021/03/17/00121615995782649133526/Foto/j14m1143.jpg',

},
{
    'name':'Antonio Perez',
    'user':'mamajuegololasos',
    'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture':'https://cflvdg.avoz.es/sc/wWrf3TUzQyWKEFzZTo3imnw4rr4=/480x/2021/03/17/00121615995782649133526/Foto/j14m1143.jpg',
},
{
    'name':'Laura Vazquez',
    'user':'lauritavr',
    'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture':'https://cflvdg.avoz.es/sc/wWrf3TUzQyWKEFzZTo3imnw4rr4=/480x/2021/03/17/00121615995782649133526/Foto/j14m1143.jpg',
}
]
def list_posts(request):
    content = []
    for post in posts:
        content.append(""" 
        <p><strong>{name}</strong></p>
        <p><small>{user} -<i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    
    return HttpResponse('<br>'.join)
# Create your views here.
