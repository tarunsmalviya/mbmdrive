from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import re

from .models import UserProfile
from .form import LoginForm, RegisterForm


def index(request):
    return render(request, 'register/index.html', {})


def user_login(request, *message):
    if request.user.is_authenticated():
        return redirect(index)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = form['email'].value()
        password = form['password'].value()

        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(index)
            else:
                message = 'You are disabled by admin!'
        else:
            message = 'Invalid username and password!'

    return render(request, 'register/login.html', {'message': message, 'form': LoginForm()})


def user_logout(request):
    logout(request)
    if request.user.is_authenticated():
        return redirect(index)
    else:
        return redirect(user_login)


def user_register(request, *message):
    if request.user.is_authenticated():
        return redirect(index)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        first_name = form['first_name'].value()
        last_name = form['last_name'].value()
        mobile = form['mobile'].value()
        email = form['email'].value()
        password = form['password'].value()

        try:
            user = User.objects.get(email=email, username=email)
            message = 'Email already exists!'
        except User.DoesNotExist:
            if re.match(r'^[789]\d{9}$', mobile) == None:
                message = 'Invalid mobile number!'
            elif last_name and last_name and mobile and email and password and re.match(r'^[789]\d{9}$', mobile):
                user = User.objects.create_user(username=email, email=email, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                UserProfile.objects.create(user=user, mobile=mobile)

                if user.pk:
                    message = 'Successfully registered!'
                else:
                    message = 'Unable to register!'
            else:
                message = 'All fields are required!'

    return render(request, 'register/register.html', {'message': message, 'form': RegisterForm()})
