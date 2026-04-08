from django import forms
from .models import PasswordEntry

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['website', 'url', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }