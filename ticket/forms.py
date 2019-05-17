from django import forms

from .models import ticKet, search


class TicketForm(forms.ModelForm):

    class Meta:
        model = ticKet
        fields = ('ticket_number', 'meter_number', 'street', 'date', 'time')


class SearchForm(forms.ModelForm):

    class Meta:
        model = search
        fields = ('weekday', 'meter_number', 'start_date', 'end_date')
