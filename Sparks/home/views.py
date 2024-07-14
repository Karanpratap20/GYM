from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login, logout

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("/Home")
    return render(request,'index.html')

def Home(request):
    return render(request,'Home.html')

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'about.html')

def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'services.html')

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method== "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Message Sent Successfully!")

    return render(request,'contact.html')

def loginUser(request):
    if request.method=="POST":
        # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request,'index.html')
        else:
            # No backend authenticated the credentialss
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

def bmi(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'bmi.html')

def signupUser(request):
    if request.method=="POST":
        # Get the post parameters
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        # check for errorneous inputs
        # username should be under 10 characters
        if len(username)>10:
            return render(request,'signup.html')
        
        # password should match
        if pass1!=pass2:
            return render(request,'signup.html')
        
        # Create the user
        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return render(request,'login.html')
    return render(request,'signup.html')
