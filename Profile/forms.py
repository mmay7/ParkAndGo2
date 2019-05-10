from django import forms
from .models import Profile



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'car', 'email_address', 'home_address', 'phone_number')
