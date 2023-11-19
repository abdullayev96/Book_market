from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def Login_page(request):
    if request.method  =="POST":
        username  = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid username')
            return redirect('login')


        user = authenticate(username=username, password=password)
        if  user is None:
            messages.error(request, 'Invalid password')
            return redirect('login')

        else:
            login(request, user)
            return redirect('home')


    return render(request, 'login.html')


def Logout_page(request):
    logout(request)
    return redirect('login')





def Register_page(request):
    if request.method  == "POST":
        first_name = request.POST.get('first_name', None)
        last_name= request.POST.get('last_name', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Already Account username")

            return redirect('register')


        user = User.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username
                                        )

        user.set_password(password)
        user.save()
        messages.info(request, "Successfully Account ")

        return redirect('login')

    return render(request, 'register.html')
