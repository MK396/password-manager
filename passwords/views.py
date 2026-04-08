from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry
from .forms import PasswordEntryForm
from .utils import encrypt_password, decrypt_password

# Create your views here.

def toggle_security(request):
    current_mode = request.session.get('security_on', False)
    request.session['security_on'] = not current_mode
    return redirect('password_list')

@login_required
def password_list(request):
    entries = PasswordEntry.objects.filter(user=request.user)

    security_on = request.session.get('security_on', False)

    # Odszyfrowanie haseł do wyświetlenia
    for entry in entries:
        entry.password_text = decrypt_password(entry.password)
    
    return render(request, 'passwords/password_list.html', {
        'entries': entries, 
        'security_on': security_on
    })

@login_required
def add_password(request):
    security_on = request.session.get('security_on', False)

    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            if security_on:
                password_entry.password = encrypt_password(password_entry.password)

            password_entry.save()
            return redirect('password_list')
    else:
        form = PasswordEntryForm()
    return render(request, 'passwords/add_password.html', {
        'form': form,
        'security_on': security_on
        })