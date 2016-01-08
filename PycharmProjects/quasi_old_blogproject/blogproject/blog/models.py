from django.db import models

class post(models.Model):
    text = models.TextField(max_length=5000)
    title= models.CharField(max_length=40)

