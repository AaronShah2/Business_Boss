from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
# Create your views here.
class LoginView(View):
    def get(self, request):
        a = 3 / 10
        context = {'a': a}
        return render(request, "boss/index.html", context)
def main(request):
    # sample of sending
    a = 3 / 10
    context = {'a': a}
    return render(request, "boss/index.html", context)

# registration form that allows user to create account
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('month')
    else:
        form = SignUpForm()
    return render(request, 'boss/reg_form.html',{'form': form})

# allows users to log into account
def login(request):
    if request.method == "POST":
        form = AuthenticationForm()
        if(request.user.is_authenticated):
            return redirect('month')
    else:
        form = AuthenticationForm()
    return render(request, 'boss/login.html', {'form': form})

# enables user data to be accessed by other variables in program
@login_required(redirect_field_name='login')
def mainAcc(request):
    return render(request, 'boss/mainAcc.html')