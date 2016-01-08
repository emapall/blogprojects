from django import forms
from models import  Tweet
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["title","text"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)

# class UserForm(forms.Form):
#     username=forms.CharField(label="Your username", max_length=30)
#     password=forms.CharField(label="Your password", widget=forms.PasswordInput)
#     email=forms.CharField(label="Your e-mail adress", widget=forms.EmailInput,required=False)
#     first_name=forms.CharField(label="Your name",required=False)
#     last_name=forms.CharField(label="Your last name",required=False)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=["username","password","email","first_name","last_name"]
        widgets={
            'password':forms.widgets.PasswordInput,
        }