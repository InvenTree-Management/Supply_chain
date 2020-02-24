from django.db import models
from django.contrib.auth.models import User


class HospitalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hospital_code = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class SupplierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class ItemCategory(models.Model):
    item_category = models.CharField(max_length=100)


class Item(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    item_code = models.CharField(max_length=50)
    manufacture_date = models.DateTimeField(auto_now=False)
    expiry_date = models.TimeField(auto_now=False)
    items_available = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name + '-' + self.item_code


class HospitalCategory(models.Model):
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)


class SupplierCategory(models.Model):
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)


class HospitalItems(models.Model):
    item_category = models.ForeignKey(HospitalCategory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class SupplierItems(models.Model):
    item_category = models.ForeignKey(SupplierCategory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


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


class SupplierOrder(models.Model):
    received = models.DateTimeField(null=True, max_length=100)
    dispatched = models.DateTimeField(null=True, max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_dispatched = models.IntegerField(default=0)
    hospital_code = models.CharField(max_length=100)

    RECEIVED = 'REC'
    DISPATCHED = 'DIS'
    PENDING = 'PEN'
    DELIVERED = 'DEL'

    STATUS_CHOICES = [
        (RECEIVED, 'Received'),
        (DISPATCHED, 'Dispatched'),
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
    ]

    SupplierStatus = models.CharField(max_length=3, choices=STATUS_CHOICES, default=RECEIVED)

    def __str__(self):
        return self.item.name