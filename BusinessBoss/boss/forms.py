from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FinancialAccount


class SignUpForm(UserCreationForm):
    # initializes integer inputs that are viewable in web browser
    salary = forms.IntegerField(required=True)
    year = forms.IntegerField(required=True)
    class Meta:
        model = FinancialAccount
        fields = ('username', 'year', 'salary', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.salary = self.cleaned_data['salary']
        user.year = self.cleaned_data['year']

        if commit:
            user.save()

        return user