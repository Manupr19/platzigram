from django.shortcuts import render
from django.http import HttpResponse

def list_posts(request):
    posts=[1,2,3]
    return HttpResponse(str(posts))
# Create your views here.
