from django.urls import path
from .views import user_orders


urlpatterns = [
    path('orders/', user_orders, name='user_orders')
]