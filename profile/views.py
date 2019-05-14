from django.shortcuts import render, redirect, get_object_or_404
from .models import proFile
from .forms import ProfileForm
from django.contrib.auth.models import User

# so the idea for this one is that it would be like the ticket_search function but it would search
# through all the profiles to see if they have the same username as the logged in user. If not it
# would redirect them to create a profile. If there was one it would return it and go into the
# profile.html thing and print it out


def profile_new(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            # get the logged in user, save the
            # fields, then saves the username from the user
            profile = form.save(commit=False)
            profile.username = request.user
            profile.save()
        return redirect('/')
    else:
        proFile.username = User.first_name
        form = ProfileForm()
    return render(request, 'profile_new.html', {'form': form})


def profile_search(request):
    currentUser = request.user
    results = proFile.objects.filter(user=currentUser)
    submitbutton = request.GET.get('submit')
    context = {'results': results, 'submitbutton': submitbutton}
    print(context)
    return render(request, 'profile/profile_info.html', context)

