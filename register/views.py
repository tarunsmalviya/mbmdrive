from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from drive.views import dashboard
from .models import UserProfile


def index(request):
    return render(request, 'register/index.html', {})


def user_login(request, *message):
    if request.user.is_authenticated():
        return redirect(dashboard)

    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(dashboard)
            else:
                message = 'You are disabled by admin!'
        else:
            message = 'Invalid username and password!'

    return render(request, 'register/login.html', {'message': message})


def user_logout(request):
    logout(request)
    if request.user.is_authenticated():
        return redirect(dashboard)
    else:
        return redirect(user_login)


def user_register(request):
    if request.method == 'POST':
        fname = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")
        mobile = request.POST.get("mobile", "")

        try:
            user = User.objects.get(username=username)
            message = 'Username already exists!'
        except User.DoesNotExist:
            if fname and lname and username and password and email and mobile:
                user = User.objects.create_user(username=username, password=password, email=email, )
                user.first_name = fname
                user.last_name = lname
                user.save()

                UserProfile.objects.create(user=user, mobile=mobile, type='P')

                if user:
                    message = 'Successfully registered!'
                else:
                    message = 'Unable to register!'
            else:
                message = 'All fields are required!'

    return redirect(user_login)
