from django.shortcuts import render, redirect  # Dodano render
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry  # Upewnij się, że masz ten import
from .forms import PasswordEntryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


@login_required
def add_password(request):
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            password_entry.save()
            return redirect('password_list')
    else:
        form = PasswordEntryForm()
    return render(request, 'passwords/add_password.html', {'form': form})

@login_required
def password_list(request):
    entries = PasswordEntry.objects.filter(user=request.user)
    return render(request, 'passwords/password_list.html', {'entries': entries})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatyczne zalogowanie po rejestracji
            return redirect('password_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})