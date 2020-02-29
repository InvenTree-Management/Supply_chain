from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

flag = 0  # for hospital


def homepage(request):
    if request.method == 'POST':
        opt = request.POST.get('submit')
        if opt == 'login':
            _username = request.POST.get('username')
            _password = request.POST.get('password')
            user = authenticate(username=_username, password=_password)
            login(request, user)
            if user is not None:
                return HttpResponse("You have successfully signed in !!")
            else:
                return render(request, 'userApp/login.html')
        elif opt == 'hosp':
            return HttpResponseRedirect(reverse('hospital_signup'))
        else:
            return HttpResponseRedirect(reverse('supplier_signup'))
    else:
        return render(request, 'userApp/login.html')


def supplier_signup(request):
    if request.method == 'POST':
        _name = request.POST.get('name')
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        _phone = request.POST.get('phone')
        _email = request.POST.get('email')
        _address = request.POST.get('address')
        user = User.objects.create_user(username=_username, password=_password, email=_email,
                                        first_name=_name)
        user.save()
        supplier_user = SupplierProfile(user=user, phone_no=_phone, address=_address)
        supplier_user.save()
        return HttpResponseRedirect(reverse('supplier_home'))

    else:
        return render(request, 'userApp/supp_signup.html')


def hospital_signup(request):
    if request.method == 'POST':
        _name = request.POST.get('name_hosp')
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        _phone = request.POST.get('phone')
        _email = request.POST.get('email')
        _address = request.POST.get('address')
        _supplier = request.POST.get('')
        user = User.objects.create_user(username=_username, password=_password, email=_email)
        user.first_name = _name
        user.save()
        hospital_user = HospitalProfile(user=user, phone_no=_phone, address=_address)
        hospital_user.save()
        return HttpResponseRedirect(reverse('hospital_home'))

    else:
        supp_list = SupplierProfile.objects.values_list('user', flat=True)
        return render(request, 'userApp/hosp_signup.html', context={'list': supp_list})


def hospital_home(request):
    if request.method == 'GET':
        user = request.user
        return render(request, 'userApp/hosp_home.html')


def supplier_home(request):
    if request.method == 'GET':
        return render(request, 'userApp/supp_home.html')
