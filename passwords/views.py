from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry
from .forms import PasswordEntryForm

# Create your views here.

@login_required
def password_list(request):
    entries = PasswordEntry.objects.filter(user=request.user)
    return render(request, 'passwords/password_list.html', {'entries': entries})

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