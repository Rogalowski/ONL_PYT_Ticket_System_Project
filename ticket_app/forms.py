from django.forms import ModelForm
from django import forms
from ticket_app.models import STATUS, PRIORITY, DEPARTMENTS, CATEGORY_PROBLEM, Ticket


# class TicketForm(forms.Form):
class TicketForm(ModelForm):
    # title = forms.CharField(required=True)
    # description = forms.CharField(required=True)
    # priorytet =
    # department_assignment
    # problem_category
    # user_requestor
    # user_assignment
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