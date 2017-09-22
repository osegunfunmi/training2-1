from django import forms
from django.forms import ModelForm


class FormGuest(ModelForm):

    class Meta:
        from src.guest.models import Guest

        model = Guest
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'enter your firstname',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'enter your last name',
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'enter an email address',
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'enter your password here',
                'class': 'form-control',
            }),
        }
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'email': "Email",
            'password': "Password"
        }
        help_texts = {
            'password': "Please enter a solid password here, and should be no less than 6 characters long"
        }