from django.db import models
from django.contrib.auth.models import User


class HospitalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hospital_code = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name


class SupplierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ManyToManyField(HospitalProfile, null=True, blank=True,)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + '-' + self.phone_no


class ItemCategory(models.Model):
    item_category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "ItemCategories"

    def __str__(self):
        return self.item_category


class Item(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    item_code = models.CharField(max_length=50)
    manufacture_date = models.DateTimeField(auto_now=False)
    expiry_date = models.TimeField(auto_now=False)
    items_available = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name + '-' + self.item_code


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    supplier = models.CharField(max_length=40)      # sender
    hospital = models.CharField(max_length=40)      # receiver
    hospital_code = models.CharField(max_length=20)
    order_time = models.DateTimeField(null=True)
    delivery_time = models.DateTimeField(null=True)

    RECEIVED = 'REC'
    REQUESTED = 'REQ'
    DISPATCHED = 'DIS'
    PENDING = 'PEN'
    DELIVERED = 'DEL'

    STATUS_CHOICES = [
        (RECEIVED, 'Received'),
        (DISPATCHED, 'Dispatched'),
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (REQUESTED, 'Requested'),
    ]
    hosp_status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='NA')
                            # five types of status : REC, REQ, DIS, PEN, DLV
    supp_status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='NA')

    def __str__(self):
        return self.item.name + '-' + self.quantity
