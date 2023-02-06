from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Phone, Brands, PhoneImage
from Cart.forms import CartAddProductForm
from Orders.models import Order, OrderItem


def phone_model(request, pk):
    cart_product_form = CartAddProductForm()
    try:
        phone = Phone.objects.all().get(pk=pk)
        images = PhoneImage.objects.filter(phone=phone)
    except Phone.DoesNotExist:
        return HttpResponseNotFound(f'object at id {pk} not found')
    return render(request, 'Products/html/phone_model.html', {'phone': phone, 'cart_product_form': cart_product_form, 'images': images})


def product_brand_list(request, brand):
    cart_product_form = CartAddProductForm()
    phones = Phone.objects.all().filter(brand__name=brand).prefetch_related('images')
    return render(request, 'Products/html/brand_phone_list.html', {'phones': phones, 'cart_product_form': cart_product_form, 'images': 'images', 'brand': brand})


def main_page(request):
    cart_product_form = CartAddProductForm()
    phones = Phone.objects.all().prefetch_related('images')
    return render(request, 'Products/html/main_page.html', {'phones': phones, 'cart_product_form': cart_product_form})                                                              