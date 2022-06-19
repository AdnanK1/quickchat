from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('logout',views.logoutUser,name='logout'),
    path('setup',views.setup,name='setup'),

    path('',views.home,name='home'),
    path('post',views.post,name='post')
]