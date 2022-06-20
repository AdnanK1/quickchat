from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginPage,name='login'),
    path('register',views.registerPage,name='register'),
    path('logout',views.logoutUser,name='logout'),
    path('setup',views.setup,name='setup'),

    path('',views.home,name='home'),
    path('post',views.postList.as_view(),name='post'),
    path('profile',views.profilePage,name='profile'),
    path('add-business',views.business,name='business'),
]