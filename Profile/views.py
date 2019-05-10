from django.shortcuts import render, redirect, get_object_or_404
from ticket.models import Ticket
from ticket.forms import TicketForm


def profile_list(request):
    ticket = Ticket.objects.order_by('ticket_number')
    return render(request, 'profile/profile_new', {'ticket': ticket})


def profile_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket/ticket_detail.html', {'ticket': ticket})


def profile_new(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
        return redirect('profile_info', pk=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'profile/profile_new.html', {'form': form})

