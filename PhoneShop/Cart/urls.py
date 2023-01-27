from django.urls import path, re_path
from .views import cart_add, cart_remove, cart_detail, cart_subtract


app_name = 'cart'


urlpatterns = [
    path('detail', cart_detail, name='cart_detail'),
    path('add/<int:phone_id>', cart_add, name='cart_add'),
    path('subtract/<int:phone_id>', cart_subtract, name='cart_subtract'),
    path('remove/<int:phone_id>', cart_remove, name='cart_remove'),
]