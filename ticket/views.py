from django.shortcuts import render, redirect, get_object_or_404
from .models import ticKet, search
from .forms import TicketForm, SearchForm


def ticket_home(request):
    return render(request, 'ticket/ticket_home.html')


def about_us(request):
    return render(request, 'ticket/about_us.html')


def tickets_list(request):
    ticket = ticKet.objects.order_by('ticket_number')
    return render(request, 'ticket/tickets_list.html', {'ticket': ticket})


def ticket_detail(request, pk):
    ticket = get_object_or_404(ticKet, pk=pk)
    return render(request, 'ticket/ticket_detail.html', {'ticket': ticket})


def ticket_new(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            user = request.user
            ticket_number = form.cleaned_data['ticket_number']
            meter_number = form.cleaned_data['meter_number']
            street = form.cleaned_data['street']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            weekday = date.weekday()
            ticket = ticKet.objects.create(user=user, ticket_number=ticket_number, meter_number=meter_number,
                                           street=street, date=date, time=time, weekday=weekday)
            ticket.save()
        return redirect('/')
    else:
        form = TicketForm()
    return render(request, 'ticket/ticket_edit.html', {'form': form})


def ticket_search_create(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            weekday_word = form.cleaned_data['weekday_word']
            meter_number = form.cleaned_data['meter_number']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            if weekday_word == 'Monday':
                weekday_num = 0
            elif weekday_word == 'Tuesday':
                weekday_num = 1
            elif weekday_word == 'Wednesday':
                weekday_num = 2
            elif weekday_word == 'Thursday':
                weekday_num = 3
            elif weekday_word == 'Friday':
                weekday_num = 4
            elif weekday_word == 'Saturday':
                weekday_num = 5
            else:
                weekday_num = 6
            searchObject = search.objects.create(weekday_word=weekday_word, weekday_num=weekday_num,
                                                 meter_number=meter_number, start_date=start_date, end_date=end_date)
            return ticket_search(request, searchObject)
    else:
        form = SearchForm()
    return render(request, 'ticket/ticket_search.html', {'form': form})


def ticket_search(request, search):

        results = ticKet.objects.filter(meter_number=search.meter_number, weekday=search.weekday_num).order_by("time")

        if results is not None:

            context = {'results': results}
            return render(request, 'ticket/ticket_search_results.html', context)

        else:
            return render(request, 'ticket/ticket_search_results.html')

