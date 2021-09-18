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
    # ticket_create.user_assignment.add(1)



@pytest.fixture
def ticket_user_assignment(ticket):  # *args, **kwargs
    # ticket = Ticket.objects.get(title='fake_title')
    # ticket = Ticket.objects.create(
    #     title='fake_title2',
    #     description='fake_description2',
    #     status='Not Acknowledged',
    #     priorytet='Low',
    #     date_creation=timezone.now(),
    #     date_update=timezone.now(),
    #     date_resolve=timezone.now(),
    #     department_assignment_id=2,
    #     problem_category_id=2,
    #     user_requestor_id=2,
    #     # user_assignment=1,
    # )
    # ticket_usr_ass = Ticket.objects.create(user_assignment=ticket.user_assignment.set(1))
    # user_assignment=User.objects.get(username='jacek').set(1),
    # Ticket.objects.create(ticket_id=1, user_id=1)
    # return ticket_usr_ass
    return ticket.user_assignment.add(1)


@pytest.fixture
def correspondence(ticket):
    return Correspondence.objects.create(
        user_id=1,
        description='Test Corespondence Description',
        date_creation=timezone.now(),
        ticket_correspondence_id=1,
    )