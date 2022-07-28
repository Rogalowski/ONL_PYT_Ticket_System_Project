from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from ticket_app.models import Ticket, Correspondence, User
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
            # 'user_requestor',  # TO DO user requestor should be logged user
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
    title = forms.CharField(label='Search by title/status', required=False)
    user_requestor = forms.ModelChoiceField(
        queryset=User.objects.all(), required=False)

    class Meta:
        model = Ticket
        fields = (
            'title',
            'user_requestor',
            # 'status',
        )
        labels = {
            "title": "Search by title/status",
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


class UserSettingsForm(forms.Form):
    # username = forms.CharField(validators=[username_validator], required=True)

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Your password', 'autocomplete': 'new-password'})
    )
    password2 = forms.CharField(
        label="Retype password",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Retype password as before', 'autocomplete': 'new-password'}),
    )
    # password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    address_city = forms.CharField(max_length=64)
    phone_number = forms.IntegerField()

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email__iexact=email)
    #     if qs.count() > 0:
    #         raise forms.ValidationError("Email address exsist, choose another", code='email_mismatch')
    #     return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            print('INNE HASLA')
            raise forms.ValidationError(
                "Password mismatch, try again", code='password_mismatch'
            )
        return password2
