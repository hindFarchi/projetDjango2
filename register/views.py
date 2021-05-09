from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from store.models import Product


# Create your views here.


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            userContext = {'user': user}
            messages.success(request, 'Account was created successfully')
            return redirect('/login/login/')
    context = {'form': form}
    return render(request, 'store/products/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            userContext = {'user': user}
            return redirect('/', userContext)
        else:
            messages.info(request, 'User Name or Password incorrect')
            return render(request, 'store/products/login.html')
    return render(request, 'store/products/login.html')
