from django import forms
from django.forms import widgets
from models import  Tweet
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text","title"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.widgets.PasswordInput)


class UserForm(forms.ModelForm):
    pass

    def is_valid(self):
        del self.password2

        super(UserForm, self).is_valid()
