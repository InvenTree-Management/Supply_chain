from django.db import models
from django.contrib.auth.models import User


class HospitalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hospital_code = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    item_code = models.CharField(max_length=50)
    manufacture_date = models.DateTimeField(auto_now=False)
    expiry_date = models.DateTimeField(auto_now=False)
    quantity_available = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name + '-' + self.item_code


class HospitalOrder(models.Model):
    requested = models.DateTimeField(null=True, max_length=100)
    received = models.DateTimeField(null=True, max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_requested = models.IntegerField(default=0)
    HospitalStatus = models.TextField(max_length=100)

    RECEIVED = 'REC'
    REQUESTED = 'REQ'

    STATUS_CHOICES = [
        (RECEIVED, 'Received'),
        (REQUESTED, 'Requested'),
    ]

    SupplierStatus = models.CharField(max_length=3, choices=STATUS_CHOICES, default=REQUESTED)

    def __str__(self):
        return self.item_name + '-' + self.quantity_requested



