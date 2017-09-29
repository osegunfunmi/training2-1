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


class FormEvent(ModelForm):

    class Meta:
        from src.guest.models import Event
        model = Event
        fields = ['event_name', 'description', 'event_date', 'location']
        widgets = {
            'event_name': forms.TextInput(attrs={
                'placeholder': 'specify the title of your event',
                'class': 'form-control',
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'describe the event 200 characters',
                'class': 'form-control',
            }),
            'event_date': forms.TextInput(attrs={
                'placeholder': 'choose a date for your event',
                'class': 'form-control',
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'event venue',
                'class': 'form-control',
            }),
        }
        labels = {
            'event_name': "Title",
            'description': "Description",
            'event_date': "Event Date",
            'location': "Venue",
        }