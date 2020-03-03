from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

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

        name = _username
        print(name)
        login(request, user)
        return redirect(f'supplier/')

        # return HttpResponseRedirect('supplier_home')

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
        _supplier = request.POST.get('user_type')
        user = User.objects.create_user(username=_username, password=_password, email=_email)
        user.first_name = _name
        user.save()
        hospital_user = HospitalProfile(user=user, phone_no=_phone, address=_address)
        hospital_user.save()

        supp_user, created = User.objects.get_or_create(username=_supplier)
        s = SupplierProfile(user=supp_user, hospital=hospital_user)
        s.save()

        return HttpResponseRedirect(reverse('hospital_home'))

    else:
        # supp_list = SupplierProfile.objects.values_list('user', flat=True)
        supp_list = SupplierProfile.objects.filter(id=6)
        return render(request, 'userApp/hosp_signup.html', context={'list': supp_list})


def hospital_home(request):
    if request.method == 'GET':
        user = request.user
        return render(request, 'userApp/hosp_home.html')


def supplier_home(request, supp_name):
    user = get_object_or_404(User, username=supp_name)
    return render(request, 'userApp/supp_home.html', {'user': user})


def profile(request):
    user = User.objects.get(username=request.user.username)
    print(user)
    print(user.first_name)
    return render(request, 'userApp/supp_home.html', {'user': user})
