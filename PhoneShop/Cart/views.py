from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
import json
from decimal import *

from Products.models import Phone
from Orders.models import OrderItem
from Orders.forms import OrderCreateForm
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, phone_id):
    cart = Cart(request)
    phone = get_object_or_404(Phone, id=phone_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(phone=phone,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, phone_id):
    cart = Cart(request)
    phone = get_object_or_404(Phone, id=phone_id)
    cart.remove(phone)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print(form.errors)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, phone=item['phone'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            return render(request, 'Orders/user_orders.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'Cart/html/cart_detail.html', {'cart': cart, 'cart_product_form': cart_product_form, 'form': form})



