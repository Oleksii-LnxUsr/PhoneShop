from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Orders.forms import OrderCreateForm
from Orders.models import Order, OrderItem


@login_required
def user_orders(request):
    orders = Order.objects.all()
    user_orders = orders.filter(user=request.user)
    for items in user_orders:
        user_order_items = OrderItem.objects.filter(order=items)
        for some in user_order_items:
            print(some.phone.model)
    form = OrderCreateForm()           
    return render(request, 'Orders/user_orders.html', {'form': form, 'orders': user_orders, 'items': user_order_items, 'model': some})