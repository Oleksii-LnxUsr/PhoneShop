from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Orders.forms import OrderCreateForm
from Orders.models import Order, OrderItem
from django import template


register = template.Library()


@login_required
def user_orders(request):
    form = OrderCreateForm()
    context = {'form': form}
    orders = Order.objects.all()
    if request.method == 'POST':
        uuid = (request.POST['package-code'])
        try:
            orders = orders.filter(uuid=uuid)
            for order in orders:
                items = OrderItem.objects.all().filter(order=order)                   
            context = {'form': form, 'orders': orders, 'items': items}
        except:
            messages.error(request, "Write valid uuid code")

    user_orders = orders.filter(user=request.user) #orders filter by request.user
    return render(request, 'Orders/user_orders.html', context)