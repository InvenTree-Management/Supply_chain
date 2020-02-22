from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'user_example/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # get that filled form

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']  # gets the username and
            password = form.cleaned_data['password1']  # and the password from the submitted form
            user = authenticate(username=username, password=password)  # check if password and userbame matches
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()  # creating object displaying empty form

    context = {'form': form}
    return render(request, 'registration/register.html', context)

