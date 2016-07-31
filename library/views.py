from django.shortcuts import render, redirect

from register.views import user_login


def library(request):
    if request.user.is_authenticated():
        return render(request, 'library/library.html', {})
    else:
        return redirect(user_login)
