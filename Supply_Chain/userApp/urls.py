from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sup', views.supplier, name='supplier'),
    #path('', views.hospital_home, name='hospital_home'),

]
