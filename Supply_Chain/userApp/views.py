from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.http import HttpResponse

flag = 0  # for hospital


def signup(request):
    if request.user.is_authenticated:
        global flag
        if flag == 0:  # we are checking for hospital
            try:
                hospital_user = HospitalProfile.objects.get(user=request.user)
            except HospitalProfile.DoesNotExist:
                hospital_user = HospitalProfile()

        elif flag == 1:  # we are checking for supplier
            try:
                supplier_user = SupplierProfile.objects.get(user=request.user)

            except SupplierProfile.DoesNotExist:
                supplier_user = SupplierProfile()

    else:
        if request.method == 'POST':
            # if request.POST['password'] == request.POST['password again']:
            _username = request.POST.get('username')
            _password = request.POST.get('password')
            user_type = request.POST.get('user_type')

            if not user_type:              # if hospital
                flag = 0
                print(flag)
                user = User.objects.create_user(username=_username, password=_password)
                hospital_user = HospitalProfile(user=user)
                hospital_user.save()

            else:  # if supplier
                flag = 1
                print(flag)
                user = User.objects.create_user(username=_username, password=_password)
                supplier_user = SupplierProfile(user=user)
                supplier_user.save()

            return HttpResponse("You have successfully signed in !!")
            # else:
            #   return render(request, 'signup.html', {'error': "Passwords don't match"})

        else:
            return render(request, "userApp/login.html")


def hospital_home(request):
    if request.method == 'GET':
        return render(request, 'userApp/hosp_home.html')


def supplier(request):
    if request.method.get == 'POST':
        return HttpResponse('Supplier added successfully')
    else:
        list = {}
        supplier = SupplierProfile.objects.all()
        for ele in supplier:
            list.append(ele.username)
        context = {'supplier_list': list}
        return render(request, 'userApp/supplier.html', context)
