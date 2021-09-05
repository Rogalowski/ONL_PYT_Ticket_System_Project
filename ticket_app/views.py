from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView

from .models import Ticket, User
from ticket_app.forms import TicketForm


class HomeView(View):
    def get(self, request):
        all_tickets = Ticket.objects.all()
        it_tickets = Ticket.objects.all().filter(department_assignment=2)
        hr_tickets = Ticket.objects.all().filter(department_assignment=3)
        pm_tickets = Ticket.objects.all().filter(department_assignment=4)
        fb_tickets = Ticket.objects.all().filter(department_assignment=5)
        context = {
            'all_tickets': all_tickets,
            'it_tickets': it_tickets,
            'hr_tickets': hr_tickets,
            'pm_tickets': pm_tickets,
            'fb_tickets': fb_tickets,
        }
        return render(request, 'ticket_app/home_view.html', context)


class TicketList(View):
    def get(self, request):

        # ticket = Ticket.objects.get(pk=kwargs['ticket_id'])  # dzieki temu mozemy sie dostac w jinja (lista iterowalna) product_detail.categories.all
        tickets = Ticket.objects.all()
        # categories = Category.objects.all() #NIE POTRZEBNE do kategorii mozemy sie odowlac przez pk=kwargs['product_id']) lub relacje
        return render(request, "ticket_app/ticket_list_view.html", {
            "tickets": tickets,
        }
                      )


class TicketCreate(View):
    def get(self, request):

        # Manual ticket creation
        # ticket_create = Ticket.objects.create(
        #     # ticket = Ticket(
        #     title='title2',
        #     description='description2',
        #     status='Pending Requestor Information',
        #     priorytet=2,
        #     department_assignment_id=4,
        #     problem_category_id=11,
        #     user_requestor_id=1,
        # )
        # ticket_create.user_assignment.add(3) # dodaje do pola many to many gfg

        context = {
            'form': TicketForm(),
        }
        return render(request, 'ticket_app/ticket_create_view.html', context)
    def post(self, request):
        form = TicketForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            print(f"Choosen: {title}")
            # status = form.cleaned_data['status']
            priorytet = form.cleaned_data['priorytet']
            print(f"Choosen: {priorytet}")
            department_assignment = form.cleaned_data['department_assignment']
            print(f"Choosen department: {department_assignment}")
            problem_category = form.cleaned_data['problem_category']
            print(f"Choosen problem: {problem_category}")
            user_requestor = form.cleaned_data['user_requestor']
            print(f"Choosen user req: {user_requestor}")
            user_assignment = form.cleaned_data['user_assignment']
            # print(f"Choosen user ass: {user_assignment }")
            # date_creation = form.cleaned_data['date_creation']
            date_update = form.cleaned_data['date_update']
            # date_resolve = form.cleaned_data['date_resolve']
            print('CHECK')
            print(*user_assignment.filter(department=department_assignment))
            print(problem_category.department.name_department)
            print(department_assignment.name_department)

            # check if Department choose is the same  department from problem category. If not it will show error
            # Problem Categroy from other department assignment is prohibet
            if department_assignment.name_department == problem_category.department.name_department:

                # ticket = Ticket.objects.create(**form.cleaned_data)
                ticket_create = Ticket.objects.create(
                # ticket = Ticket(
                    title=title,
                    description=description,
                    # status=status,
                    priorytet=priorytet,
                    department_assignment=department_assignment,
                    problem_category=problem_category,
                    user_requestor=user_requestor,
                    # date_creation=date_creation,
                    # date_update=date_update,
                    # date_resolve=date_resolve,
                )
                ticket_create.user_assignment.add(*user_assignment.filter(department=department_assignment))
                return redirect('ticket_list')
            else:
                context = {
                    'form': form,
                    'result': f"ASSIGNED DEPT SHOULD HAVE SAME DEPT PROBLEM"
                }
                return render(request, 'ticket_app/ticket_create_view.html', context)

        context = {
            'form': form,
            'result': f"SOMETHING GOES WRONG"
        }
        return render(request, 'ticket_app/ticket_create_view.html', context)
        # return redirect('home_index')
            # return render(request, 'ticket_app/home_view.html', context)
            # return redirect('tickets', ticket_id=Ticket.objects.all().get(id=ticket_id)


class TicketView(View):
    def get(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(id=kwargs['ticket_id'])
        context = {
                    'ticket': ticket,
                }
        return render(request, 'ticket_app/ticket_view.html', context)



# class TicketEditView(UpdateView):
#     def get(self, request, *args, **kwargs):
#         ticket = Ticket.objects.get(id=kwargs['ticket_id'])
#         context = {
#             'form': TicketForm(),
#             'ticket': ticket,
#         }
#         return render(request, 'ticket_app/ticket_create_view.html', context)
class TicketEditView(UpdateView):
    template_name = 'ticket_app/ticket_create_view.html'
    # form_class = ProductForm

    fields = [
        'title',
        'description',
        'status',
        'priorytet',
        'department_assignment',
        'problem_category',
        'user_requestor',
        'user_assignment',
    ]  # wybrane pola
    model = Ticket

    def get_object(self, queryset=None):  # pobranie url_id z urls.py na zmineinaym modelu Notice w ID
        id_ = self.kwargs.get("ticket_id")
        return get_object_or_404(Ticket, id=id_)

    def get_success_url(self):
        return reverse('ticket_list') # , kwargs=['ticket_id']
