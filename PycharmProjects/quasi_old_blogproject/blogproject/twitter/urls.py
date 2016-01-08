from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^tweets/(?P<utente>\w+)/$', views.visualizza_post, name='visualizza_post'),
    url(r'^choose/$', views.scegli_user),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^crea/$',views.crea_tweet),
]