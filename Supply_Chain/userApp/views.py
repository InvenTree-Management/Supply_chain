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
            username = request.POST.get('username')
            password = request.POST.get('password')
            x = request.POST.get('optradio')

            if x == 0:  # if hospital
                flag = 0
                print(flag)
                hospital_user = HospitalProfile(username=username, password=password)
                hospital_user.save()

            elif x == 1:  # if supplier
                flag = 1
                print(flag)
                supplier_user = SupplierProfile(username=username, password=password)
                supplier_user.save()

            return HttpResponse("You have successfully signed in !!")
            # else:
            #   return render(request, 'signup.html', {'error': "Passwords don't match"})

        if request.method == 'GET':
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
