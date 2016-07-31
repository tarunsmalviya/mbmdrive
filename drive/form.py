from django import forms
from django.contrib.auth.models import User

from .models import DriveFile


class UploadForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Name", 'autofocus': 'autofocus',
                                      'required': True, 'max_length': 150}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Description", 'autofocus': 'autofocus',
                                     'required': True, 'max_length': 500}))
    file = forms.FileField(
        widget=forms.FileInput(attrs={'class': "form-control input-group", 'placeholder': "File", 'required': True}))

    class Meta:
        model = DriveFile
        fields = ('name', 'description', 'file',)


class DeleteForm(forms.Form):
    file_id = forms.CharField(widget=forms.HiddenInput(attrs={'required': True}))
