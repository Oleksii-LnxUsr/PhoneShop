from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Phone, Brands
from Cart.forms import CartAddProductForm
from Orders.models import Order

def phone_model(request, pk):   
    cart_product_form = CartAddProductForm()
    try:
        phone = Phone.objects.all().get(pk=pk)
    except Phone.DoesNotExist:
        return HttpResponseNotFound(f'object at id {pk} not found')
    return render(request, 'Products/html/phone_model.html', {'phone': phone, 'cart_product_form': cart_product_form})



def product_brand_list(request, brand):
    phones = Phone.objects.all().filter(brand__name=brand)
    return render(request, 'Products/html/brand_phone_list.html', {'phones': phones})



def main_page(request):
    phones = Phone.objects.all()
    return render(request, 'Products/html/main_page.html', {'phones': phones})
