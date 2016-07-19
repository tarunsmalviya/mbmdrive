from django.shortcuts import render, redirect


def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'drive/dashboard.html', {})
    else:
        return redirect('register.views.user_login')
