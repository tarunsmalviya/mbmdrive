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
        email = request.POST.get("email", "")
        password = request.POST.get("inputPassword", "")

        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(dashboard)
            else:
                message = 'You are disabled by admin!'
        else:
            message = 'Invalid username and password!'

    return render(request, 'register/login.html', {'message': message })


def user_logout(request):
    logout(request)
    if request.user.is_authenticated():
        return redirect(dashboard)
    else:
        return redirect(user_login)


def user_register(request, *message):
    if request.method == 'POST':
        fname = request.POST.get("inputFname", "")
        lname = request.POST.get("inputLname", "")
        mobile = request.POST.get("inputMobile", "")
        email = request.POST.get("inputEmail", "")
        password = request.POST.get("inputPassword", "")

        try:
            user = User.objects.get(email=email)
            message = 'Email already exists!'
        except User.DoesNotExist:
            if fname and lname and mobile and email and password:
                user = User.objects.create_user(email=email, password=password)
                user.first_name = fname
                user.last_name = lname
                user.save()

                UserProfile.objects.create(user=user, mobile=mobile)

                if user.pk:
                    message = 'Successfully registered!'
                else:
                    message = 'Unable to register!'
            else:
                message = 'All fields are required!' + fname + ' | ' + lname + ' | ' + mobile + ' | ' + email + ' | ' + password

    return render(request, 'register/register.html', {'message': message})
