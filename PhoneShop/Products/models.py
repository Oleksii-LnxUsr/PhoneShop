from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=50)
    describe = models.TextField()
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.name


class Phone(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    model = models.CharField(max_length=100)
    describe = models.TextField()
    color = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.model

    class Meta:
        db_table = 'phones'


class PhoneImage(models.Model):
    phone = models.ForeignKey(Phone, related_name='images',default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.phone.model