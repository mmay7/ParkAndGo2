from django.shortcuts import render, redirect, get_object_or_404
from .models import profile
from .forms import ParkingProfileForm
from django.contrib.auth.models import User

# so the idea for this one is that it would be like the ticket_search function but it would search
# through all the profiles to see if they have the same username as the logged in user. If not it
# would redirect them to create a information. If there was one it would return it and go into the
# information.html thing and print it out


def profile_new(request):
    if request.method == "POST":
        form = ParkingProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            car = form.cleaned_data['car']
            email = form.cleaned_data['email_address']
            home = form.cleaned_data['home_address']
            phone = form.cleaned_data['phone_number']

            information = profile.objects.create(user=user, first_name=first, last_name=last,
            car=car, email_address=email, home_address=home, phone_number=phone)
            information.save
        return redirect('/')
    else:
        profile.username = User.first_name
        form = ParkingProfileForm()
    return render(request, 'profile_new.html', {'form': form})


def profile_search(request):
    currentUser = request.user
    results = profile.objects.filter(user=currentUser)
    submitbutton = request.GET.get('submit')
    context = {'results': results, 'submitbutton': submitbutton}
    print(context)
    return render(request, 'profile/profile_info.html', context)

