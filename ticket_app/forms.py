from django.forms import ModelForm
from django import forms
from ticket_app.models import Ticket,  Correspondence
from django.forms import ModelForm


# Ticket Form with added fields that will needed (class Meta) in form
class TicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = (
            'title',
            'description',
            'status',
            'priorytet',
            'department_assignment',
            'problem_category',
            'user_requestor',  # TO DO user requestor should be logged user
            # 'user_assignment',  Automatically set for logged user in class View
        )
        widgets = {'status': forms.HiddenInput()}  # hidden as have default set
        exclude = ('date_creation',)


# Ticket update form
class TicketUpdateForm(ModelForm):

    class Meta:
        model = Ticket
        fields = (
            'title',
            'description',
            'status',
            'priorytet',
            'department_assignment',
            'problem_category',
            'user_requestor',
            'user_assignment',
        )
        exclude = ('date_creation',)


# Ticket search form
class TicketSearchForm(ModelForm):
    title = forms.CharField(required=False)

    class Meta:
        model = Ticket
        fields = (
            'title',
            'user_requestor',
            # 'status',
        )
        labels = {
            "title": ("Search by title/status"),
        }


# Ticket Coresspondence Form
class TicketCorespondenceForm(ModelForm):
    class Meta:
        model = Correspondence
        fields = (
            # 'user',   logged user in View class
            'description',
        )


# User Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
