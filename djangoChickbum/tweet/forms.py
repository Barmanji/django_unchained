from typing import override

from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Forms are useful for taking django power for handling html forms
class TweetForm(forms.ModelForm):
  class Meta: # we have to use meta
    model = Tweet
    fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
