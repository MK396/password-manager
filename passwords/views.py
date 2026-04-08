from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry

# Create your views here.

@login_required
def password_list(request):
    entries = PasswordEntry.objects.filter(user=request.user)
    return render(request, 'passwords/password_list.html', {'entries': entries})
