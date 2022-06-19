from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('logout',views.logoutUser,name='logout'),

    path('',views.home,name='home'),
    path('setup',views.setup,name='setup'),
]