from django.forms import ModelForm
from django import forms
from ticket_app.models import STATUS, PRIORITY, DEPARTMENTS, CATEGORY_PROBLEM, Ticket, User
from django.forms import MultiValueField, Textarea, ModelForm, TextInput, CharField, ChoiceField

# class TicketForm(forms.Form):
#     title = forms.CharField(required=True)
#     description = forms.CharField(widget=forms.TextInput, required=True)
#     priorytet = forms.ChoiceField(widget=forms.RadioSelect(), choices=PRIORITY, required=True)
#     department_assignment = forms.ChoiceField(widget=forms.RadioSelect(), choices=DEPARTMENTS, required=True)
#     problem_category = forms.ChoiceField(widget=forms.RadioSelect(), choices=CATEGORY_PROBLEM, required=True)
#     user_requestor = forms.ChoiceField(widget=forms.Select,
#                                               choices=User.objects.all().values_list('id', 'username'),
#                                               required=True)
#     user_assignment = forms.ChoiceField(widget=forms.SelectMultiple,
#                                               choices=User.objects.all().values_list('pk', 'username'),
#                                               required=True)

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'title',
            'description',
            # 'status',
            'priorytet',
            'department_assignment',
            'problem_category',
            'user_requestor',
            'user_assignment',
        )

class TicketUpdateForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'title',
            'description',
            # 'status',
            'priorytet',
            'department_assignment',
            'problem_category',
            'user_requestor',
            'user_assignment',
        )
    # def to_internal_value(self, data):
    #     # check for "date_resolve": "" and convert to None
    #     if data['date_resolve'] == '':
    #         data['date_resolve'] = None
    #     return super(TicketForm, self).to_internal_value(data)

# class TicketUpdateForm(ModelForm):
#     class Meta:
#         model = Ticket
#         fields = (
#             'title',
#             'description',
#             'status',
#             'priorytet',
#             # 'department_assignment',
#             'problem_category',
#             'user_requestor',
#         )