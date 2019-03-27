from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm
from django.db.models import Q




def ticket_home(request):
    return render(request, 'ticket/ticket_home.html')


def tickets_list(request):
    ticket = Ticket.objects.order_by('ticket_number')
    return render(request, 'ticket/tickets_list.html', {'ticket': ticket})


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket/ticket_detail.html', {'ticket': ticket})


def ticket_new(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
        return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'ticket/ticket_edit.html', {'form': form})


def ticket_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query) | Q(content__icontains=query)

            #Ticket.objects.filter(meter_number = query)
            results = Ticket.objects.filter(lookups).distinct()

            context = {'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'ticket/ticket_search.html', context)

        else:
            return render(request, 'ticket/ticket_search.html')

    else:
        return render(request, 'ticket/ticket_search.html')
