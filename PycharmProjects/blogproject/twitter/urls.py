from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$',views.welcome,name="welcome"),
    url(r'^tweets/(?P<utente>\w+)/$', views.home, name='home'),
    url(r'^tweets/$', views.home_launcher, name='home_launcher'),
    url(r'^choose/$', views.scegli_user,name='sciegli_user'),
    url(r'^crea/$',views.crea_tweet,name="crea_tweet"),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^logout/$',views.logout_view,name="logout"),
    url(r'registra/$',views.create_user,name="registrazione"),
]