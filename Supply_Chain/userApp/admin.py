from django.contrib import admin
from .models import *

admin.site.register(HospitalProfile)
admin.site.register(HospitalCategory)
admin.site.register(HospitalItems)
admin.site.register(HospitalOrder)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(SupplierProfile)
admin.site.register(SupplierCategory)
admin.site.register(SupplierItems)
admin.site.register(SupplierOrder)

