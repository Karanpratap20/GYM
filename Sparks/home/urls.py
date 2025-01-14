from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Home', views.Home, name='Home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('bmi',views.bmi,name='bmi'),
    path('signup',views.signupUser,name="signup"),
]
