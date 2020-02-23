from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from hospital_app.models import HospitalProfile
from supplier_app.models import SupplierProfile
import datetime
import random

flag = 0  # for hospital


# def homepage(request):
#    return render(request, 'authen/homepage.html')


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
                # phone_no = request.POST.get('Phone No')
                # address = request.POST.get('address')
                hospital_user = HospitalProfile(username=username, password=password)
                hospital_user.save()

            elif x == 1:  # if supplier
                flag = 1
                # phone_no = request.POST.get('Phone No')
                # address = request.POST.get('address')
                supplier_user = SupplierProfile(username=username, password=password)
                supplier_user.save()

            # else:
            # #return render(request, 'signup.html', {'error': "Passwords don't match"})

        else:
            return render(request, 'authenticate/signup.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/hospital_app/')
        # user is already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        x = request.POST.get('optradio')

        if x == 0:  # if hospital
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/hospital_app/')
            else:
                return render(request, 'authenticate/login.html', {'error': "Sorry! Cannot login"})
                # return an invalid login message

        elif x == 1:  # if supplier
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/supplier_app/')
            else:
                return render(request, 'authenticate/login.html', {'error': "Sorry! cannot login"})

    else:
        return render(request, 'authenticate/login.html')



