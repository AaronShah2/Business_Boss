from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


class SignUpForm(UserCreationForm):
    salary = forms.IntegerField(required=True)
    year = forms.IntegerField(required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'year', 'salary', 'password1', 'password2', )