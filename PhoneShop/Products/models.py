from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=50)
    describe = models.TextField()
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.name


class Phone(models.Model):
    images = models.ImageField(upload_to='images/')
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    model = models.CharField(max_length=100)
    describe = models.TextField()
    color = models.CharField(max_length=30)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.model


    class Meta:
        db_table = 'phones'
    