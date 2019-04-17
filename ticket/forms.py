from django import forms

from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('name', 'ticket_number', 'meter_number', 'street', 'date', 'time')
