from django.shortcuts import render, redirect, get_object_or_404
from .models import ticKet
from .forms import TicketForm
from django.db.models import Q


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


def ticket_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        results = ticKet.objects.filter(meter_number=query).order_by("time")

        if results is not None:

            context = {'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'ticket/ticket_search.html', context)

        else:
            return render(request, 'ticket/ticket_search.html')

    else:
        return render(request, 'ticket/ticket_search.html')

