from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('product_list')
            else:
                return redirect('home')
        else:
            return render(request, 'registration/login.html', {"message": "invalid username or password"})
    return render(request, 'registration/login.html')


def user_creation(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
        else:
            context={"form":form}
            return render(request, 'accounts/user_reg.html', context)
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/user_reg.html', {'form': form})