from django.contrib import auth, messages
from users.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import redirect, render


def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Fill in all the fields')
            return redirect('/auth/register')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'A user with this name already exists')
            return redirect('/auth/register')
        try:
            user = User.objects.create_user(username=username,
                        email=email,
                        password=password)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Registration completed successfully')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Internal system error!!')
            return redirect('/auth/register')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if not user:
             messages.add_message(request, constants.ERROR, 'Wrong password or username')
             return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/')

def exit(request):
    auth.logout(request)
    return redirect('/auth/login')
