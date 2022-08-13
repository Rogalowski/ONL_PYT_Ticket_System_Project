import datetime

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.conf import settings

from .models import Department, Ticket, User, Correspondence
from ticket_app.forms import TicketForm, TicketUpdateForm, \
    TicketSearchForm, TicketCorespondenceForm, UserLoginForm, UserSettingsForm


#  Main View of site. It shows department urls that redirect to department
#  queue list of tickets
class HomeView(View):
    def get(self, request):
        all_tickets = Ticket.objects.all()
        #count available ticket on each department
        exclude_list = ['Resolved Successfull', 'Dropped']
        it_tickets = Ticket.objects.all().filter(department_assignment=2).exclude(status__in=exclude_list)
        hr_tickets = Ticket.objects.all().filter(department_assignment=3).exclude(status__in=exclude_list)
        pm_tickets = Ticket.objects.all().filter(department_assignment=4).exclude(status__in=exclude_list)
        fb_tickets = Ticket.objects.all().filter(department_assignment=5).exclude(status__in=exclude_list)

        context = {
            'all_tickets': all_tickets,
            'it_tickets': it_tickets,
            'hr_tickets': hr_tickets,
            'pm_tickets': pm_tickets,
            'fb_tickets': fb_tickets,
        }
        if request.user.is_anonymous:
            pass
        else:
            logged_user = request.user.username
            print(logged_user)

            context = {
                'all_tickets': all_tickets,
                'it_tickets': it_tickets,
                'hr_tickets': hr_tickets,
                'pm_tickets': pm_tickets,
                'fb_tickets': fb_tickets,
            }
            return render(request, 'ticket_app/home_view.html', context)
        return render(request, 'ticket_app/home_view.html', context)



# Views of queue tickets departments. Paginator added to scrolling tickets page by page.
# Implemented search form for tickets in post method
class TicketList(View):
    def get(self, request, department):

        exclude_list = ['Resolved Successfull', 'Dropped']
        # .exclude(name__in=exclude_list)
        global tickets
        if department == "IT":
            tickets = Ticket.objects.all().filter(department_assignment=2).exclude(status__in=exclude_list)
        elif department == "HR":
            tickets = Ticket.objects.all().filter(department_assignment=3).exclude(status__in=exclude_list)
        elif department == "PM":
            tickets = Ticket.objects.all().filter(department_assignment=4).exclude(status__in=exclude_list)
        elif department == "FB":
            tickets = Ticket.objects.all().filter(department_assignment=5).exclude(status__in=exclude_list)
        elif department == 'ALL':
            tickets = Ticket.objects.all()

        paginator = Paginator(tickets, 6)  # max number of objects on page
        page = request.GET.get('page')
        ticket_pages = paginator.get_page(page)

        context = {
            "ticket_pages": ticket_pages,
            'department': department,
            'form': TicketSearchForm,
            'tickets': tickets,
        }
        return render(request, "ticket_app/ticket_list_view.html", context)

    # Post method for search form. Search implemented by ticket title/status/user requester.
    def post(self, request, *args, **kwargs):
        form = TicketSearchForm(request.POST)
        context = {
            'form': form,
            'title': [],
            'status': [],
        }
        if form.is_valid():
            typed_name = form.cleaned_data['title']
            typed_user = form.cleaned_data['user_requestor']

            filter_ticket_title = {'title__icontains': typed_name}  # filtering by typed title
            filter_ticket_status = {'status__icontains': typed_name}  # filtering by typed status
            # filter_ticket_requester = {
            #     'user_requestor__username__icontains': typed_user.username  # filtering by typed user
            # }

            if not typed_user:
                tickets = Ticket.objects.filter(Q(**filter_ticket_title) |
                                                Q(**filter_ticket_status)).order_by('title').distinct()
            else:
                tickets = Ticket.objects.filter(Q(**filter_ticket_title) |
                                                Q(**filter_ticket_status)).filter(
                    user_requestor__username__icontains=typed_user.username
                ).order_by('title').distinct()

            paginator = Paginator(tickets, 6)  # max number of objects on page
            page = request.GET.get('page')
            ticket_pages = paginator.get_page(page)

            context['ticket_pages'] = ticket_pages
        return render(request, 'ticket_app/ticket_list_view.html', context)


# Designed View for New Ticket Creation
# Anonymous users will be automatically redirect to log in view
class TicketCreate(LoginRequiredMixin, View):
    def get(self, request):
        # MANUAL TICKET CREATION:
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
        # ticket_create.user_assignment.add(3) # dodaje do pola many to many

        context = {
            'form': TicketForm(),
        }
        return render(request, 'ticket_app/ticket_create_view.html', context)

    # Post method for sent post request and save on database
    def post(self, request):
        form = TicketForm(request.POST or None)
        context = {
            'form': form,
        }
        if form.is_valid():
            title = form.cleaned_data['title']  # get provided title by user from form
            description = form.cleaned_data['description']
            print(f"Choosen: {title}")  # Test get title from form, etc below
            priorytet = form.cleaned_data['priorytet']
            print(f"Choosen: {priorytet}")
            department_assignment = form.cleaned_data['department_assignment']
            print(f"Choosen department: {department_assignment}")
            problem_category = form.cleaned_data['problem_category']
            print(f"Choosen problem: {problem_category}")


            logged_user = User.objects.get(username=request.user.username)
            # Check if chosen Department is the same as department from problem category:
            # If not, will show error. Problem Categroy from other department assignment is prohibet
            if department_assignment.name_department == problem_category.department.name_department:
                # ticket = Ticket.objects.create(**form.cleaned_data)
                ticket_create = Ticket.objects.create(
                    title=title,
                    description=description,
                    # status=status,        Status should be default on creation new ticket
                    priorytet=priorytet,
                    department_assignment=department_assignment,
                    problem_category=problem_category,
                    user_requestor=logged_user,
                )

                # Will add all selected users_assigned to tt from selected department
                # (other users will be missed)
                # ticket_create.user_assignment.add(
                #     *user_assignment.filter(department=department_assignment)
                #     )

                # Will add all users_assign to tt from selected department
                ticket_create.user_assignment.add(
                    *User.objects.filter(department_id=department_assignment.pk)
                )
                return redirect('ticket_list', department_assignment.name_department)
            else:
                context = {
                    'form': form,
                    'result': f"ASSIGNED DEPARTMENT SHOULD HAVE ASSIGNED SAME DEPARTMENT OF PROBLEM"
                }
                return render(request, 'ticket_app/ticket_create_view.html', context)

        context = {
            'form': form,
            'result': f"FORM CRUSHED, TRY ONE MORE TIME"
        }
        return render(request, 'ticket_app/ticket_create_view.html', context)


# View details of ticket, with correspondence list on each ticket
# and correspondence form to add new comments
class TicketView(View):
    def get(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(id=kwargs['ticket_id'])
        correspondence = Correspondence.objects.filter(ticket_correspondence_id=ticket.pk)
        context = {
            'ticket': ticket,
            'correspondence': correspondence,
            'form': TicketCorespondenceForm(),
                }
        return render(request, 'ticket_app/ticket_view.html', context)

    # Post method for correspondence form, to add new correspondence/comments.
    # For anonymous users, has hidden form on HTML side
    def post(self, request, *args, **kwargs):
        form = TicketCorespondenceForm(request.POST or None)
        if form.is_valid():
            logged_user = User.objects.get(username=request.user.username)
            # user = form.cleaned_data['user']  # requestor of correspondence should be logged
            description = form.cleaned_data['description']

            ticket_correspondence = Ticket.objects.get(id=kwargs['ticket_id'])
            Correspondence.objects.create(
                user=logged_user,  # logged user will be assigned
                description=description,
                ticket_correspondence_id=ticket_correspondence.pk
            )
            return redirect('ticket', ticket_correspondence.pk)
        context = {
            'form': form,
            'result': f"FORM CRUSHED, PLEASE TRY ONE MORE TIME"
        }
        return render(request, 'ticket_app/ticket_corespon_create_view.html', context)


# Ticket Edit view that require Logged user.
# Anonymous users will be automatically redirect to log in view
class TicketEditView(LoginRequiredMixin, UpdateView):
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

    # Will try get cuurent object by id. If not, will show E404
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("ticket_id")
        return get_object_or_404(Ticket, id=id_)

    # Success url will redirect after success edit
    def get_success_url(self):
        return reverse('ticket_list')  # , kwargs=['ticket_id']

    def post(self, request, *args, **kwargs):
        form = TicketUpdateForm(request.POST or None)
        logged_user = User.objects.get(username=request.user.username)
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
            print(problem_category.department.name_department)
            print(department_assignment.name_department)
            print("AS", user_assignment.filter(department__name_department__icontains=department_assignment))

            # Check if Department choose is the same  department from problem category.
            # Check if Department choose is the same as user assigned department
            # If not it will show error
            # Problem Category from other department assignment is prohibet
            if (department_assignment.name_department == problem_category.department.name_department) and \
                    (user_assignment.filter(department__name_department__icontains=department_assignment)):

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

                # Ticket update fields
                ticket_update = Ticket.objects.get(id=kwargs['ticket_id'])
                ticket_update.title = title
                ticket_update.description = description
                ticket_update.status = status
                ticket_update.priorytet = priorytet
                ticket_update.department_assignment = department_assignment
                ticket_update.problem_category = problem_category
                ticket_update.user_requestor = user_requestor

                # If user looged select another requester it will add information in title
                if user_requestor != logged_user:
                    ticket_update.title = title + f"  [ON BEHALF: {logged_user}]"
                if status == "Dropped" or 'Resolved Successfull':
                    ticket_update.date_resolve = datetime.datetime.now()
                # Ticket save updated fields to database
                ticket_update.save()
                # user_assignment.set - will clear old entries and add selected
                ticket_update.user_assignment.set(
                    user_assignment.filter(department=department_assignment)
                )
                # ticket_update.user_assignment.clear()
                # ticket_update.user_assignment.add(
                #     *user_assignment.filter(department=department_assignment)
                # )
                return redirect('ticket_list', 'ALL')
            else:
                context = {
                    'form': form,
                    'result': f"ASSIGNED DEPARTMENT AND USER SHOULD HAVE ASSIGNED SAME DEPARTMENT OF PROBLEM"
                }
                return render(request, 'ticket_app/ticket_create_view.html', context)

        context = {
            'form': form,
            'result': f"FORM CRUSHED, TRY ONE MORE TIME"
        }
        return render(request, 'ticket_app/ticket_create_view.html', context)



class CorrespondenceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'ticket_app/correspondence_confirm_delete.html'
    model = Correspondence
    fields = ['description']

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse('ticket', kwargs={'ticket_id': self.kwargs['ticket_id']})

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('correspondence_id')
        return get_object_or_404(Correspondence, id=id_)


# User login form view
class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'auth/login_user_view.html', {
        'form': form
        })

    # post method for login, needed correct username and password
    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            # if user typed correct passes will redirect to home view
            # if not will ask for try one more time
            if user is not None:
                login(request, user)
                return redirect('home_index')
            else:
                attempt = request.session.get("attempt") or 0
                request.session['attempt'] = attempt + 1
                wrong_passes = f"Wrong login or password! Try again {attempt}!"
                context = {
                    'form': form,
                    'wrong_passes': wrong_passes,
                }
                return render(request, 'auth/login_user_view.html', context)


# Logout view
class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home_index')


# User details view, need Logged user
class UserDetailsView(LoginRequiredMixin, View):
    def get(self, request, current_user):
        print(f"current: {current_user}")
        user_detail = User.objects.get(username=current_user)
        print(f"Logged {user_detail} ")
        context = {
            'user_detail': user_detail,
            'current_user': current_user,
        }
        return render(request, 'auth/user_details_view.html', context)


# Logged user settings form edit view, need Logged user.
# Will check if user from url is equal as logged to make sure chage of logged user settings
class UserSettingsEditView(LoginRequiredMixin, View):
    def get(self, request, current_user):

        logged_user = User.objects.get(username=request.user.username)
        print(f'Current: {current_user}')
        print(f'Logged: {logged_user}')
        if logged_user.username == current_user:  # Protection from edit settings another non logged user
            user_detail = User.objects.filter(username=current_user).values()[0]
            context = {
                'form': UserSettingsForm(user_detail),
                'current_user': current_user,
            }
            return render(request, 'auth/user_create_view.html', context)
        else:
            context = {
                'form': UserLoginForm,
                'wrong_passes': 'IF YOU WANT CHANGE SETTINGS ANOTHER USER, PLEASE LOGIN FIRST',
            }
            return render(request, 'auth/login_user_view.html', context)

    def post(self, request, current_user):
        form = UserSettingsForm(request.POST or None)

        if form.is_valid():

            password1 = make_password(form.cleaned_data['password1'])


            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            address_city = form.cleaned_data['address_city']
            phone_number = form.cleaned_data['phone_number']
            # user = authenticate(username=username, password=password)

            user_update = User.objects.get(username=current_user)
            # if user_update.check_password(password1) != password1:
            #     print(f'{user_update.check_password(password1)}')
            #     print(f'TO SAMO HASLO, NIE ZAPISALEM DO BAZY')
            #     return redirect('user_edit_settings', current_user)
            # else:
            user_update.password = password1


            user_update.first_name = first_name
            user_update.last_name = last_name
            # user_update.email = email
            user_update.address_city = address_city
            user_update.phone_number = phone_number

            user_update.save()
            print('ZAPISANO')

            return redirect('user_logout_home')
        return redirect('user_edit_settings', current_user)


from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from Ticket_System_Project.tokens import account_activation_token

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Aktywacja konta na stronie ODDAM W DOBRE RĘCE'

    email_body = render_to_string('auth/activate.html', {
        'user': user,
        # 'domain': 'donation.rogalowski.uk:30157',
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_FROM_USER,
        to=[user.email]
    )
    email.send()


def activate_user(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if user and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True
        user.save()

        messages.add_message(
            request, messages.ERROR, 'Email zweryfikowany poprawnie, możesz się zalogować :)')
        return redirect('home_view')

    messages.add_message(request, messages.ERROR,
                         f'Użytkownik źle zweryfikowany, prawdopodobnie aktywny!')
    return redirect('register_view')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):



        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        # department = request.POST.get('department')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            password2 = make_password(password)
        else:
            messages.add_message(
                request, messages.ERROR, f'Podane hasła różnią się od siebie, spróbuj jeszcze raz!')
            return render(request, 'register.html')
        # try :
        #     np = NumericPasswordValidator()
        #     np.validate(password)
        # except ValidationError
        #     messages.add_message()

        # print(department)
        # depart = Department.objects.all().filter(id=department)
        # print(depart)
        try:
            user = User.objects.create(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,
                # department=depart,
                password=password2,
                is_active=False,
            )
        except:
            messages.add_message(
                request, messages.ERROR, f'Użytkownik już istnieje, spróbuj jeszcze raz!')
            return render(request, 'register.html')

        send_activation_email(user, request)
        return redirect('home_index')
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
