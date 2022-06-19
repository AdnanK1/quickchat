from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)

def loginPage(request):
    context = {}
    return render(request,'auth/login.html',context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save()
            login(request,user,backend = 'django.contrib.auth.backends.ModelBackend')
            
            return redirect('home')
        else:
            messages.error(request,'An error has occurred when Logging, please use a stronger password')
    context = {'form':form}
    return render(request,'auth/register.html',context)