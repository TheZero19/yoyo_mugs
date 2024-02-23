from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from restaurant.models import Order

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

        messages.success(request, f'Account created for { username }! You are now able to log in!')
        return redirect('login')

    else:
        return render(request, "users/register.html")

def users_logout(request):
    return render(request, "users/logout.html")

def users_orders(request):
    orders = Order.objects.all()
    for order in orders:
        total_price = sum(item.itemPPU for item in order.items.all())
        setattr(order, 'total_price', total_price)
    return render(request, "users/orders.html", context={'orders': orders})