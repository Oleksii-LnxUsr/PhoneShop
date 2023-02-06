from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from decimal import *
import json

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

@require_POST
def cart_subtract(request, phone_id):
    cart = Cart(request)
    phone = get_object_or_404(Phone, id=phone_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.subtract(phone=phone,
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
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            send_mail(
                subject=f'{order.user.username} PhoneShop',
                message=f'{order.first_name} Thanks you for order, uuid of order {order.uuid}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[order.user.email])

            for item in cart:
                Phone_quantity = Phone.objects.get(id=item['phone'].id)
                Phone_quantity.quantity = Phone_quantity.quantity-item['quantity']
                Phone_quantity.save()
                OrderItem.objects.create(order=order, phone=item['phone'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'Orders/user_orders.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'Cart/html/cart_detail.html', {'cart': cart, 'cart_product_form': cart_product_form, 'form': form})
