from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)

def loginPage(request):
    context = {}
    return render(request,'auth/login.html',context)

def registerPage(request):
    context = {}
    return render(request,'auth/register.html',context)