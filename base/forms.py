from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . import models

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class SetUpForm(ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'
        exclude = ['user','email']

class PostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'
        exclude = ['author']

class UserUpdateform(ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'
        exclude = ['user','email','national_id']