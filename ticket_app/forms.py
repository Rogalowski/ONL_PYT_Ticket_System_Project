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


# Logged user settings Form
# class UserSettingsForm(ModelForm):
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'password',
#             'first_name',
#             'last_name',
#             'email',
#             'address_city',
#             'phone_number',
#         )

# def username_validator(username):
#     if User.objects.filter(username=username).exists():
# raise ValidationError('Username already exist', code='invalid')
class UserSettingsForm(forms.Form):
    # username = forms.CharField(validators=[username_validator], required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    # password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address_city = forms.CharField(max_length=64)
    phone_number = forms.IntegerField()

