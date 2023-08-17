from django.db import models
from main.models import Product


class Orders(models.Model):
    STATE_CHOICES = (
        ('NotProcessed', 'Not Processed'),
        ('InProgress', 'InProgress'),
        ('Processed', 'Processed'),
    )
    user_name = models.CharField('Name', max_length=100)
    user_surname = models.CharField('Surname', max_length=100)
    email = models.EmailField('Email')
    number_phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, through='OrderItem')
    state = models.CharField('State', max_length=20, choices=STATE_CHOICES, default='NotProcessed')


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity product')
