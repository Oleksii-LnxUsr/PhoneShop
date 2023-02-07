from .models import Order
from django.shortcuts import render


def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'Orders/user_orders.html', {'orders': orders})