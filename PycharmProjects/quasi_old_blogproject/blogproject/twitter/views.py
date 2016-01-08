from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import TweetForm, LoginForm
from .models import Tweet
from django.contrib.auth.models import User

def scegli_user(request):
    # utenti=[]
    # posts=Tweet.objects.all()
    #
    # for i in posts:
    #     utenti.append(i.user)
    #
    return render(request,"sciegli_utente.html", {"users":User.objects.all()})

def login_view(request):
    if(request.method=="GET"):
        logform=LoginForm()
        return render(request,"login.html",{'form':logform})
    if(request.method=="POST"):
        logform=LoginForm(request.POST)
        if(logform.is_valid()):
            logform=logform.cleaned_data
            user = authenticate(username='john', password='secret')
                if user is not None:

def visualizza_post(request, utente):

    print utente

    posts=Tweet.objects.filter(Q(user__username=utente) |  Q(user__follower_set__follower__username=utente))
    print(type(posts))
    return render(request,"tweets.html",{'tweets':posts} )


def crea_tweet(request):
    print( request.method)
    if(request.method == 'GET'):
        cont = TweetForm()
        return render(request,"crea.html",{"form":cont})

    if(request.method == 'POST'):
        print request