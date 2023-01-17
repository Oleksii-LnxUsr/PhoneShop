import uuid
from django.db import models

from Users.models import CustomUser
from Products.models import Phone


class Order(models.Model):
    PACKAGE_STATUS = (
        ('Prepare', 'Prepare to deliver'),
        ('In the way', 'Your package in the way'),
        ('Delivered', 'Your package delivered'),
    )   
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    package_status = models.CharField(choices=PACKAGE_STATUS, max_length=25, default='Prepare', null=True, blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):    
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    
    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity