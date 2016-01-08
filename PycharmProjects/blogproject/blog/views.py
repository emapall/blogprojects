# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render

from models import post


def hello_world(request):
    name = request.GET.get('name','word') #se non c'e' il primo parametro, restituise il secondo
    return HttpResponse("Hello world!".format(name))

#def hello_name(request, name):
#    return HttpResponse("Hello {}!".format(name))

def _factorial(n):
    if n==0:
        return 1
    else:
        if n>0:
            return _factorial(n-1)*n
        else:
            return -1

def factorial(request, numero=None):
    numero = request.GET.get('x', numero)
    return HttpResponse(_factorial(int(numero)))

#----------------------------------------------------
#		LEZIONE DEL VERO POST DINAMICO	
#(non cancello la cosa soprastante perchè può sempre servire e poi non la ho
#nemmeno scritta io
#--------------------------------------------------------


def blog(request):
    posts= post.objects.all()

    print posts
    return render(request, "blog.html",
                  {'posts':posts})