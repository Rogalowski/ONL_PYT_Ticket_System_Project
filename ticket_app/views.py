from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView

from .models import Ticket, User, Correspondence
from ticket_app.forms import TicketForm, TicketUpdateForm, TicketSearchForm, TicketCorespondenceForm


class HomeView(View):
    def get(self, request):
        all_tickets = Ticket.objects.all()
        #count available ticket on each department
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
    def get(self, request, department):

        global tickets
        if department == "IT":
            tickets = Ticket.objects.all().filter(department_assignment=2).exclude(status='Resolved Successfull')
        elif department == "HR":
            tickets = Ticket.objects.all().filter(department_assignment=3).exclude(status='Resolved Successfull')
        elif department == "PM":
            tickets = Ticket.objects.all().filter(department_assignment=4).exclude(status='Resolved Successfull')
        elif department == "FB":
            tickets = Ticket.objects.all().filter(department_assignment=5).exclude(status='Resolved Successfull')
        elif department == 'ALL':
            tickets = Ticket.objects.all()

        paginator = Paginator(tickets, 6)  # wysw. liczbe wierszy na stronie
        page = request.GET.get('page')
        ticket_pages = paginator.get_page(page)

        context = {
            # "tickets": tickets,
            "ticket_pages": ticket_pages,
            'department': department,
            'form': TicketSearchForm,
        }
        # ticket = Ticket.objects.get(pk=kwargs['ticket_id'])  # dzieki temu mozemy sie dostac w jinja (lista iterowalna) product_detail.categories.all

        # categories = Category.objects.all() #NIE POTRZEBNE do kategorii mozemy sie odowlac przez pk=kwargs['product_id']) lub relacje
        return render(request, "ticket_app/ticket_list_view.html", context)

    def post(self, request, *args, **kwargs):
        form = TicketSearchForm(request.POST)
        context = {
            'form': form,
            'title': [],
            'status': [],
        }
        if form.is_valid():
            # logika biznezowa np. zapis do bazy
            typed_name = form.cleaned_data['title']
            typed_user = form.cleaned_data['user_requestor']

            filter_ticket_title = {'title__icontains': typed_name}
            filter_ticket_status = {'status__icontains': typed_name}
            filter_ticket_requester = {'user_requestor__username__icontains': typed_user}
            tickets = Ticket.objects.filter(Q(**filter_ticket_title) | Q(**filter_ticket_status) and Q(**filter_ticket_requester)).order_by('title').distinct()
            # tickets2 = Ticket.objects.filter(user_requestor__username=typed_user)
            # tickets = Ticket.objects.filter(title__icontains=title)
            # status = Ticket.objects.filter(status__icontains=status)

            paginator = Paginator(tickets, 3)  # wysw. liczbe wierszy na stronie
            page = request.GET.get('page')
            ticket_pages = paginator.get_page(page)

            # context['tickets'] = tickets
            context['ticket_pages'] = ticket_pages

            # context['status'] = status

        return render(request, 'ticket_app/ticket_list_view.html', context)


class TicketCreate(View):
    def get(self, request):
        # MANUAL TICKET CREATION:
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
            # user_assignment = form.cleaned_data['user_assignment']
            # print(f"Choosen user ass: {user_assignment }")
            # date_creation = form.cleaned_data['date_creation']
            # date_update = form.cleaned_data['date_update']
            # date_resolve = form.cleaned_data['date_resolve']
            print('CHECK')
            # print(*user_assignment.filter(department=department_assignment))
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
                # Will add all selected users_assignet to tt from selected department (other users will missed)
                # ticket_create.user_assignment.add(*user_assignment.filter(department=department_assignment))

                # Will add all users_assign to tt from selected department
                ticket_create.user_assignment.add(*User.objects.filter(department_id=department_assignment.pk))
                return redirect('ticket_list', 'ALL')
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
        corespondence = Correspondence.objects.filter(ticket_correspondence_id=ticket.pk)
        context = {
            'ticket': ticket,
            'corespondence': corespondence,
            'form': TicketCorespondenceForm(),
                }
        return render(request, 'ticket_app/ticket_view.html', context)

    def post(self, request, *args, **kwargs):
        form = TicketCorespondenceForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            description = form.cleaned_data['description']

            print(f"Choosen: {user}")
            print(f"Choosen: {description}")
            print(Ticket.objects.get(id=kwargs['ticket_id']))

            ticket_correspondence = Ticket.objects.get(id=kwargs['ticket_id'])
            Correspondence.objects.create(
                user=user,
                description=description,
                ticket_correspondence_id=ticket_correspondence.pk
            )
            return redirect('ticket', ticket_correspondence.pk)
            # return render(request, 'ticket_app/ticket_create_view.html', context)

        context = {
            'form': form,
            'result': f"SOMETHING GOES WRONG"
        }
        return render(request, 'ticket_app/ticket_corespon_create_view.html', context)


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

    def post(self, request, *args, **kwargs):
        form = TicketUpdateForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            print(f"Choosen: {title}")
            status = form.cleaned_data['status']
            priorytet = form.cleaned_data['priorytet']
            print(f"Choosen: {priorytet}")
            department_assignment = form.cleaned_data['department_assignment']
            print(f"Choosen department: {department_assignment}")
            problem_category = form.cleaned_data['problem_category']
            print(f"Choosen problem: {problem_category}")
            user_requestor = form.cleaned_data['user_requestor']
            print(f"Choosen user req: {user_requestor}")
            user_assignment = form.cleaned_data['user_assignment']
            # user_assignment = request.POST.get('user_assignment')
            # user_assignment = request.POST.getlist('user_assignment')
            print(f"Choosen user ass: {user_assignment }")
            # date_creation = form.cleaned_data['date_creation']
            # date_update = form.cleaned_data['date_update']
            # date_resolve = form.cleaned_data['date_resolve']
            print('CHECK')
            # print(*user_assignment.filter(department=department_assignment))
            print(problem_category.department.name_department)
            print(department_assignment.name_department)

            # check if Department choose is the same  department from problem category. If not it will show error
            # Problem Categroy from other department assignment is prohibet
            if department_assignment.name_department == problem_category.department.name_department:

                # ticket = Ticket.objects.create(**form.cleaned_data)
                # ticket_update = Ticket(
                # # ticket_update = Ticket.objects.update_or_create(
                # # ticket_update = Ticket.objects.update(
                #     id=kwargs['ticket_id'],
                #     title=title,
                #     description=description,
                #     status=status,
                #     priorytet=priorytet,
                #     department_assignment=department_assignment,
                #     problem_category=problem_category,
                #     user_requestor=user_requestor,
                # )
                # ticket_update.user_assignment.clear() # clering all assignments before (after creation or last update)
                # ticket_update.save()
                # # ticket_update.user_assignment.add(*user_assignment)
                # ticket_update.user_assignment.add(*user_assignment.filter(department=department_assignment))

                ticket_update = Ticket.objects.get(id=kwargs['ticket_id'])
                ticket_update.title = title
                ticket_update.description = description
                ticket_update.status = status
                ticket_update.priorytet = priorytet
                ticket_update.department_assignment = department_assignment
                ticket_update.problem_category = problem_category
                ticket_update.user_requestor = user_requestor

                ticket_update.save()
                ticket_update.user_assignment.set(user_assignment.filter(department=department_assignment))

                # ticket_update.user_assignment.clear()
                # ticket_update.user_assignment.add(*user_assignment.filter(department=department_assignment))
                return redirect('ticket_list', 'ALL')
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


#
# #MOZNA USUNAC, PRAWIDLOWY TICKET EDIT VIEW2
# class TicketEditView(View):
#     def get(self, request, *args, **kwargs):
#         ticket = Ticket.objects.filter(id=kwargs['ticket_id']).values()[0] # ADD FILLED VALUES FROM OBJECT TO EDIT
#         # ticket = Ticket.objects.get(id=kwargs['ticket_id'])
#
#         context = {
#             'form': TicketUpdateForm(ticket),
#             # 'form': TicketUpdateForm(),
#             'ticket': ticket,
#         }
#         return render(request, 'ticket_app/ticket_create_view.html', context)
#
#
#     def post(self, request, *args, **kwargs):
#         form = TicketUpdateForm(request.POST)
#
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             print(f"Choosen: {title}")
#             status = form.cleaned_data['status']
#             priorytet = form.cleaned_data['priorytet']
#             print(f"Choosen: {priorytet}")
#             department_assignment = form.cleaned_data['department_assignment']
#             print(f"Choosen department: {department_assignment}")
#             problem_category = form.cleaned_data['problem_category']
#             print(f"Choosen problem: {problem_category}")
#             user_requestor = form.cleaned_data['user_requestor']
#             print(f"Choosen user req: {user_requestor}")
#             user_assignment = form.cleaned_data['user_assignment']
#             # user_assignment = request.POST.get('user_assignment')
#             # user_assignment = request.POST.getlist('user_assignment')
#             print(f"Choosen user ass: {user_assignment }")
#             # date_creation = form.cleaned_data['date_creation']
#             # date_update = form.cleaned_data['date_update']
#             # date_resolve = form.cleaned_data['date_resolve']
#             print('CHECK')
#             # print(*user_assignment.filter(department=department_assignment))
#             print(problem_category.department.name_department)
#             print(department_assignment.name_department)
#
#             # check if Department choose is the same  department from problem category. If not it will show error
#             # Problem Categroy from other department assignment is prohibet
#             if department_assignment.name_department == problem_category.department.name_department:
#
#                 # ticket = Ticket.objects.create(**form.cleaned_data)
#                 # ticket_update= Ticket(
#                 # # ticket_update = Ticket.objects.update_or_create(
#                 # # ticket_update = Ticket.objects.update(
#                 #     id=kwargs['ticket_id'],
#                 #     title=title,
#                 #     description=description,
#                 #     status=status,
#                 #     priorytet=priorytet,
#                 #     department_assignment=department_assignment,
#                 #     problem_category=problem_category,
#                 #     user_requestor=user_requestor,
#                 #     # user_assignment=user_assignment,
#                 #     # date_creation=date_creation,
#                 #     # date_update=date_update,
#                 #     # date_resolve=date_resolve,
#                 # )
#                 # ticket_update.user_assignment.clear() # clering all assignments before (after creation or last update)
#                 # ticket_update.save()
#                 #
#                 # # ticket_update.user_assignment.add(*user_assignment)
#                 # ticket_update.user_assignment.add(*user_assignment.filter(department=department_assignment))
#                 # usr = Ticket.objects.filter(user_assignment__department=department_assignment)
#                 # filtered = filter(lambda score: score >= 70, user_assignment)
#
#
#
#                 # LUBB
#                 ticket_update = Ticket.objects.get(id=kwargs['ticket_id'])
#                 ticket_update.title = title
#                 ticket_update.description = description
#                 ticket_update.status = status
#                 ticket_update.priorytet = priorytet
#                 ticket_update.department_assignment = department_assignment
#                 ticket_update.problem_category = problem_category
#                 ticket_update.user_requestor = user_requestor
#                 #
#                 ticket_update.save()
#                 # ticket_update.user_assignment.clear()
#                 ticket_update.user_assignment.set(user_assignment.filter(department=department_assignment))
#
#
#                 return redirect('ticket_list', 'ALL')
#             else:
#                 context = {
#                     'form': form,
#                     'result': f"ASSIGNED DEPT SHOULD HAVE SAME DEPT PROBLEM"
#                 }
#                 return render(request, 'ticket_app/ticket_create_view.html', context)
#
#         context = {
#             'form': form,
#             'result': f"SOMETHING GOES WRONG"
#         }
#         return render(request, 'ticket_app/ticket_create_view.html', context)

# SEPERATED CORESPONDENCE CREATION VIEW
# class TicketCorespondenceCreate(View):
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': TicketCorespondenceForm(),
#         }
#         return render(request, 'ticket_app/ticket_corespon_create_view.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = TicketCorespondenceForm(request.POST)
#
#         if form.is_valid():
#             user = form.cleaned_data['user']
#             description = form.cleaned_data['description']
#
#             print(f"Choosen: {user}")
#             print(f"Choosen: {description}")
#             print(Ticket.objects.get(id=kwargs['ticket_id']))
#
#             ticket_correspondence = Ticket.objects.get(id=kwargs['ticket_id'])
#             Correspondence.objects.create(
#                 user=user,
#                 description=description,
#                 ticket_correspondence_id=ticket_correspondence.pk
#             )
#             return redirect('ticket', ticket_correspondence.pk)
#             # return render(request, 'ticket_app/ticket_create_view.html', context)
#
#         context = {
#             'form': form,
#             'result': f"SOMETHING GOES WRONG"
#         }
#         return render(request, 'ticket_app/ticket_corespon_create_view.html', context)
