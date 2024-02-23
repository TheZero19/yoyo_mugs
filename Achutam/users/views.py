from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from restaurant.models import Order, MenuItem, MenuItemType

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
    print("View function called")
    if request.method == "POST":
        selected_items = request.POST.getlist('items')
        print(selected_items)
        total_price = 0  # Initialize total price

        items = []
        for selected_item in selected_items:
            item = MenuItem.objects.filter(itemName__iexact = selected_item).first()
            total_price+=item.itemPPU
            items.append(item)

        print(items)
        print(total_price)
        # Create a new order
        order = Order.objects.create(
            customer=request.user,
            total_price=total_price,
            isPending=True  # Assuming the order is pending by default
        )
        order.items.set(items)
        messages.success(request, "Your order has been requested!")
        return HttpResponse(total_price)
    else:
        orders = Order.objects.all()
        menu_item_types = MenuItemType.objects.all()
        menu_items = MenuItem.objects.all()
        for order in orders:
            total_price = sum(item.itemPPU for item in order.items.all())
            setattr(order, 'total_price', total_price)
        return render(request, "users/orders.html", context={'orders': orders, 'menu_items': menu_items, 'menu_item_types': menu_item_types})