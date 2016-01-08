from django.contrib.auth.models import User
from django.db import models

class Tweet(models.Model):
	text = models.TextField(max_length=500)
	title = models.CharField(max_length=30)
	created = models.DateTimeField(auto_now=True)
	user= models.ForeignKey(User)
	#update= models.DateTimeField()

	class Meta:
		ordering = ["-created"]


class Amicizia(models.Model):
	follower = models.ForeignKey(User, related_name='followed_set')
	followed = models.ForeignKey(User, related_name='follower_set')
	data_amicizia = models.DateTimeField(auto_now=True)

