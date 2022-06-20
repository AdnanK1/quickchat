from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import CreateUserForm,SetUpForm,PostForm,UserUpdateform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .email import send_welcome_email
from .models import Client,Business,Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit  import CreateView

# Create your views here.
@login_required(login_url='login')
def home(request):
    business = Business.objects.all()

    context = {}
    return render(request,'home.html',context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist ')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {'page':page}
    return render(request,'auth/login.html',context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            send_welcome_email(username,email)
            user = form.save()
            login(request,user,backend = 'django.contrib.auth.backends.ModelBackend')
            messages.success(request,f'Hello {username} you have been logged and a welcome email has been sent')
            return redirect('setup')
        else:
            messages.error(request,'An error has occurred when Logging, please use a stronger password')
    context = {'form':form}
    return render(request,'auth/register.html',context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def setup(request):
    form = SetUpForm()
    if request.method == 'POST':
        form = SetUpForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.email = request.user.email
            post.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'auth/setup.html',context)

class postList(LoginRequiredMixin,CreateView):
    def get(self,request,*args,**kwargs):
        post = Post.objects.all()
        form = PostForm()
        context = {'post':post,'form':form}

        return render(request,'post.html',context)

    def post(self,request,*args,**kwargs):
        post = Post.objects.all()
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = self.request.user.profile
            new_post.save()
            return redirect('post')
        
        context = {'post':post,'form':form}
        return render(request,'post.html',context)

@login_required(login_url='login')
def profilePage(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def business(request):
    context = {}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def updateProfile(request):
    profile = request.user.profile
    form = UserUpdateform(instance=profile)
    if request.method == 'POST':
        form = UserUpdateform(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
    
    context = {'profile':profile,'form':form}
    return render(request,'update.html',context)
