import pytest
from django.utils import timezone

from ticket_app.models import Ticket, Department, User, Correspondence, DepartmentProblem


#Plik conftest fixtury - globalnie widoczne wszedzie
@pytest.fixture
def department():
    return Department.objects.create(
        name_department='IT',
        desc_department='IT Department'
    )


@pytest.fixture
def department_problem():
    return DepartmentProblem.objects.create(
        department_id=1,
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
        department_id=1
    )


@pytest.fixture
def ticket():
    return Ticket.objects.create(
        title='fake_title1',
        description='fake_description1',
        status='Not Acknowledged',
        priorytet='Low',
        date_creation=timezone.now(),
        date_update=timezone.now(),
        date_resolve=timezone.now(),
        department_assignment_id=1,
        problem_category_id=1,
        ticket_user_requestor=1
        # user_requestor_id=1,
        # user_requestor=User.objects.get(username='jacek'),
        # user_assignment=1,
    )
    # ticket_create.user_assignment.add(1)



@pytest.fixture
def ticket_user_assignment():
    # ticket = Ticket.objects.get(title='fake_title')
    ticket = Ticket.objects.create(
        title='fake_title2',
        description='fake_description2',
        status='Not Acknowledged',
        priorytet='Low',
        date_creation=timezone.now(),
        date_update=timezone.now(),
        date_resolve=timezone.now(),
        department_assignment_id=2,
        problem_category_id=2,
        user_requestor_id=2,
        # user_assignment=1,
    )

    ticket_usr_ass = Ticket.objects.create(user_assignment=ticket.user_assignment.set(1))
    # user_assignment=User.objects.get(username='jacek').set(1),
    # Ticket.objects.create(ticket_id=1, user_id=1)
    # return ticket_usr_ass
    return ticket.user_assignment.set(1)


@pytest.fixture
def correspondence():
    return Correspondence.objects.create(
        user_id=1,
        description='Test Corespondence Description',
        date_creation=timezone.now(),
        ticket_correspondence_id=1,
    )
