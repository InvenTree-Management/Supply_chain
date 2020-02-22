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
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name + '-' + self.item_code


