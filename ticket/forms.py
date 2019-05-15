from django import forms

from .models import ticKet


class TicketForm(forms.ModelForm):

    class Meta:
        model = ticKet
        fields = ('ticket_number', 'meter_number', 'street', 'date', 'time')
