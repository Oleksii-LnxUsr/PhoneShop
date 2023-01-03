from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserForm
from django.contrib.auth.forms import AuthenticationForm


def registration_user(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(request.POST)

            form.save()
            return redirect('/')
    return render(request, 'Users/html/registration.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST) 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    form = AuthenticationForm()      
    return render(request, 'Users/html/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')

