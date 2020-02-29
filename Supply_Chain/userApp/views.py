from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.http import HttpResponse

flag = 0  # for hospital
supplier_user = SupplierProfile()
'''
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

'''


def index(request):
    if request.user.is_authenticated:
        global flag
        if not flag:
            try:
                hospital_user = HospitalProfile.objects.get(user=request.user)
            except HospitalProfile.DoesNotExist:
                hospital_user = HospitalProfile()
        elif flag == 1:  # we are checking for supplier
            try:
                supplier_user1 = SupplierProfile.objects.get(user=request.user)
            except SupplierProfile.DoesNotExist:
                supplier_user1 = SupplierProfile()

    if request.method == "POST":
        if request.POST.get("submit") == "sign_in":
            # sign_in logic goes here
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            # successfully logged in

            return HttpResponse("You have successfully logged in!")

        elif request.POST.get("submit") == "sign_up":
            # sign_up logic goes here
            uname = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('Address')
            phone = request.POST.get('phone')

            user_type = request.POST.get('type')

            if user_type == "Hospital":
                flag = 0
                print(flag)
                user = User.objects.create_user(username=uname, password=password)
                hospital_user = HospitalProfile(user=user, phone_no=phone, address=address)
                hospital_user.save()

                return HttpResponse("Your sign up is done Bro!")

            elif user_type == "Suppliers":
                flag = 1
                print(flag)
                user = User.objects.create_user(username=uname, password=password)
                global supplier_user
                supplier_user = SupplierProfile(user=user, phone_no=phone, address=address)
                #supplier_user.save()
                return render(request, 'userApp/supplier_home.html')
                #return HttpResponse("Your sign up is done Bro!")

    else:
        return render(request, "userApp/login.html")


def hospital_home(request):
    if request.method == 'GET':
        return render(request, 'userApp/hosp_home.html')


'''def supplier(request):
    if request.method == 'POST':
        return HttpResponse('Supplier added successfully')
    else:
        list = []
        supplier = SupplierProfile.objects.all()
        for ele in supplier:
            list.append(ele.username)
        context = {'supplier_list': list}
        return render(request, 'userApp/supplier.html', context)
'''


def supplier(request):
    if request.method == 'POST':
        global supplier_user
        try:
            hosp = request.POST.get('hosp')
        except hosp.ValueError:
            hosp = 4
            supplier_user = SupplierProfile(hospital=hosp)
            supplier_user.save()
        return HttpResponse("sign up done!!")
    else:
        hlist = HospitalProfile.objects.all()
        return render(request, 'userApp/supplier_home.html', context={'list': hlist})