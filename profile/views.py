from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import ProfileForm


def profile_detail(request):
    profile = get_object_or_404(Profile)
    return render(request, 'profile/profile_detail.html', {'profile': profile})


def profile_new(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile_detail.html')
    else:
        form = ProfileForm()
    return render(request, 'profile_new.html', {'form': form})

