from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (first_name and last_name and username and password):
            return HttpResponse('All fields are required!')

        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username is already taken!')

        new_user = User.objects.create_user(username = username, password = password, email= email)
        new_user.save()

        # Optionally, authenticate the user and log them in immediately
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        messages.success(request, f'Account created for { username }!')
        return redirect('restaurant-index')

    else:
        return render(request, "users/register.html")