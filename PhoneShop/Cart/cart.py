from django.contrib import messages
from django.http import HttpResponse
from decimal import Decimal
from django.conf import settings
from Products.models import Phone


class Cart(object):

    def __init__(self, request):
        ''' Initializing the cart '''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # save empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, phone, quantity=1, update_quantity=False):
        ''' Add phone to cart and update quantity '''
        phone_id = str(phone.id)
        if phone_id not in self.cart:
            self.cart[phone_id] = {'quantity': 0,
                                     'price': str(phone.price)}
        if update_quantity:
            self.cart[phone_id]['quantity'] = quantity
        else:
            phone_quantity = Phone.objects.get(id=phone_id).quantity
            if self.cart[phone_id]['quantity'] < phone_quantity:
                self.cart[phone_id]['quantity'] += quantity
            else:
                self.cart[phone_id]['quantity'] == quantity
        self.save()
        
    def subtract(self, phone, quantity=1, update_quantity=False):
        ''' Subtract phone from cart and update quantity '''
        phone_id = str(phone.id)
        if update_quantity:
            self.cart[phone_id]['quantity'] = quantity
        else:
            if self.cart[phone_id]['quantity'] > quantity:
                self.cart[phone_id]['quantity'] -= quantity
            else:
                self.cart[phone_id]['quantity'] == quantity
        self.save()

    def save(self):
        ''' Save changes in cart '''
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, phone):
        ''' Remove phone from cart '''
        phone_id = str(phone.id)
        if phone_id in self.cart:
            del self.cart[phone_id]
            self.save()

    def __iter__(self):
        ''' Iterate through the items in the cart and get the products '''
        phone_ids = self.cart.keys()
        phones = Phone.objects.filter(id__in=phone_ids).prefetch_related('images', 'brand')
        for phone in phones:
            self.cart[str(phone.id)]['phone'] = phone

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
 
    def __len__(self):
        ''' Counting all items in the cart '''
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        ''' Counting total price in cart '''
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        ''' Delete cart from session '''
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True