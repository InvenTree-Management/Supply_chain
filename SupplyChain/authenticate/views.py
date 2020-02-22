from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from hospitalapp.models import Hospital_Profile
from supplierapp.models import Supplier_Profile

flag = 0  # for hospital

def homepage(request):
    return render(request, 'authen/homepage.html')


def signup(request):
    if request.user.is_authenticated:
        global flag
        if flag == 0:  # we are checking for hospital
            try:
                hospital_user = Hospital_Profile.objects.get(user=request.user)
            except Hospital_Profile.DoesNotExist:
                Hospital_user = Hospital_Profile()

        elif flag == 1:  # we are checking for supplier
            try:
                supplier_user = Supplier_Profile.objects.get(user=request.user)

            except Supplier_Profile.DoesNotExist:
                supplier_user = Supplier_Profile()

    else:
        if request.method == 'POST':
            if request.POST['password'] == request.POST['password again']:
                username = request.POST.get('username')
                password = request.POST.get('password')
                x = request.POST.get('optradio')

                if x == 0:     # if hospital
                    flag = 0
                    hospital_user = Hospital_Profile(username=username,password=password)
                    hospital_user.save()

                elif x == 1: # if supplier
                    flag = 1
                    supplier_user = Supplier_Profile(username=username,password=password)
                    supplier_user.save()


            else:
                return render(request, 'signup.html', {'error':"Passwords don't match"})

        else:
            return render(request, 'signup.html')


