from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
   # path('hospital/', include('hospital_app.urls')),
    #path('supplier/', include('supplier_app.urls')),

]
