from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Property
from .forms import PropertyForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def property_list(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, 'properties/list.html', {'properties': properties})


@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            return redirect('home')
    else:
        form = PropertyForm()
    return render(request, 'properties/add.html', {'form': form})
