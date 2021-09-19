import pytest
from django.utils import timezone

from django.test import Client
from ticket_app.models import Ticket, Department, User, Correspondence, DepartmentProblem


#Plik conftest fixtury - globalnie widoczne wszedzie
@pytest.fixture
def department():
    return Department.objects.create(
        name_department='IT',
        desc_department='IT Department'
    )


@pytest.fixture
def department_problem(department):
    return DepartmentProblem.objects.create(
        department=department,
        category_problem='Desktops/Software'
    )

@pytest.fixture
def user():
    return User.objects.create(
        username='jacek',
        password='jacek',
        first_name='Jacek',
        last_name='Rogowski',
        email='jacek@jacek.com',
        is_staff=True,
        is_active=True,
        date_joined=timezone.now(),
        address_city='Szczecin',
        phone_number='111222333',
    )


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def ticket(department_problem, department, user):
    return Ticket.objects.create(
        title='fake_title1',
        description='fake_description1',
        status='Not Acknowledged',
        priorytet='Low',
        date_creation=timezone.now(),
        date_update=timezone.now(),
        date_resolve=timezone.now(),
        department_assignment=department,
        problem_category=department_problem,
        user_requestor=user,
        # user_requestor=User.objects.get(username='jacek'),
    )


@pytest.fixture
def ticket_user_assignment(ticket, user, department_problem, department):  # *args, **kwargs
    ticket = Ticket.objects.create(
        title='fake_title1',
        description='fake_description1',
        status='Not Acknowledged',
        priorytet='Low',
        date_creation=timezone.now(),
        date_update=timezone.now(),
        date_resolve=timezone.now(),
        department_assignment=department,
        problem_category=department_problem,
        user_requestor=user,
        user_assignment=ticket.user_assignment.set(user),
    )
    ticket1 = ticket.user_assignment.set(user.id)
    user_assign_ticket = Ticket.objects.get(username='jacek')
    # return user_assign_ticket.user_assignment.add(user.id)
    return ticket



@pytest.fixture
def correspondence(ticket, user):
    return Correspondence.objects.create(
        user=user,
        description='Test Corespondence Description',
        date_creation=timezone.now(),
        ticket_correspondence=ticket,
    )
