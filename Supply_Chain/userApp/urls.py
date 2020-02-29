from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('supp_sign', views.supplier_signup, name='supplier_signup'),
    path('hosp_sign', views.hospital_signup, name='hospital_signup'),
    path('hosp', views.hospital_home, name='hospital_home'),
    path('supp', views.supplier_home, name='supplier_home'),
]
