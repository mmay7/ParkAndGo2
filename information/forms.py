from django import forms
from .models import profile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ParkingProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('first_name', 'last_name', 'car', 'email_address', 'home_address', 'phone_number')
