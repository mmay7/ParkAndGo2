from django import forms
from .models import proFile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = proFile
        fields = ('first_name', 'last_name', 'car', 'email_address', 'home_address', 'phone_number')
