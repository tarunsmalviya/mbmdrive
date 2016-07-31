from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class': "form-control", 'placeholder': "Email address", 'autofocus': 'autofocus',
                   'required': True, 'max_length': 30}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Password", 'required': 'required'}))

    class Meta:
        model = User
        fields = ('email', 'password',)


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "First name", 'autofocus': 'autofocus',
                                      'required': True, 'max_length': 30}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Last name", 'autofocus': 'autofocus',
                                      'required': True, 'max_length': 30}))
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", 'placeholder': "Mobile number", 'autofocus': 'autofocus',
                   'required': True, 'max_length': 10,}))
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class': "form-control", 'placeholder': "Email address", 'autofocus': 'autofocus',
                   'required': True, 'max_length': 30}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Password", 'required': 'required'}))
