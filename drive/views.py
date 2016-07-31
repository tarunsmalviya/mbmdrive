from django.shortcuts import render, redirect

from register.views import user_login
from .models import DriveFile
from .form import UploadForm, DeleteForm


def mydrive(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                d = form.save()
                d.user = request.user
                d.save()

        return render(request, 'drive/mydrive.html',
                      {'file_list': DriveFile.objects.filter(user=request.user), 'form': UploadForm(),
                       'delete_form': DeleteForm()})
    else:
        return redirect(user_login)


def delete_drive_file(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = DeleteForm(request.POST)
            if form.is_valid():
                file_id = form.cleaned_data['file_id']

                f = DriveFile.objects.get(pk=file_id)
                f.delete()

        return redirect(mydrive)
    else:
        return redirect(user_login)
