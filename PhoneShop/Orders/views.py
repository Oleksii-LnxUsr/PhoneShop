from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Orders.forms import OrderCreateForm


@login_required
def user_orders(request):
    form = OrderCreateForm()
    return render(request, 'Orders/user_orders.html', {'form': form})