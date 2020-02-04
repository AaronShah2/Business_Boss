from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from datetime import date

#Current date will be found & set as the default date for application
year_ = date.today().year

# Create your models here.
# Registers User
class FinancialAccount(AbstractUser):

    # fields the account will need
    salary = models.IntegerField(default = 0)
    year = models.IntegerField(default=year_)

    REQUIRED_FIELDS = [
        'salary',
        'year']

    def __str__(self):
        return f"username: {self.username}, salary: {self.salary}, year: {self.year}"

