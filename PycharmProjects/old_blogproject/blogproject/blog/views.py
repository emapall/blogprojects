from django.http import HttpResponse
from django.shortcuts import render
from models import post


# Create your views here.


def hello_world(request):
    name=request.GET.get('name', 'world')
    return HttpResponse("Hello {}!".format(name))

def hello_name(request, name):
    return HttpResponse("Hello {}!".format(name))

def fact(request):
    num=int(request.GET.get('x', '1'))
    f=1
    for i in range(1,num+1):
        f=f*i
    return HttpResponse("Fattoriale = {}!".format(f))


def post_list(request):
    s=''

def blog (request):
    post = Post.objects.all()
    that_post = posts [0]
    return render(request,'blog.html',{
    'post': that_posts
    })