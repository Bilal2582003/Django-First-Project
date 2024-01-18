from contextlib import _RedirectStream
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
   return render(request,"signup.html")
def login(request):
   return render(request,"login.html")

def newUser(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
     # Check if passwords match
    if password == confirm_password:
            # Create a new user
        data = {
            'name':username,
            'email':email,
            'password':password
        }
        user = User.objects.create(**data)

            # Redirect to the login page
        return redirect('login')  # Use the appropriate URL name for your login page
    else:
        return redirect('signup')

    return render(request, 'login.html')
  

def userLogin(request):
   
    username = request.POST.get('username')
    password = request.POST.get('password')

        # Authenticate the user
    user = User.objects.filter(name=username,password = password)

    if user :
            # If authentication is successful, log the user in
        # login(request, user)
            # Redirect to a success page or any other desired page
        return HttpResponse('dashboard')  # Update 'dashboard' with the appropriate URL name
    else:
            # Authentication failed, handle the error (e.g., display an error message)
        return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')