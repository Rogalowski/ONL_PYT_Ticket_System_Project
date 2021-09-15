import pytest
from django.utils import timezone

from ticket_app.models import Ticket, Department, User, Correspondence


#Plik conftest fixtury - globalnie widoczne wszedzie
@pytest.fixture
def department():
    return Department.objects.create(
        name_department='IT',
        desc_department='IT Department'
    )


@pytest.fixture
def department_problem():
    return Department.objects.create(
        department_id=1,
        category_problem='Desktops/Software'
    )


@pytest.fixture
def user():
    return User.objects.create(
        username='jacek',
        first_name='Jacek',
        last_name='Rogowski',
        email='jacek@jacek.com',
        is_staff=True,
        is_active=True,
        date_joined=timezone.now(),
        address_city='Szczecin',
        phone_number='111222333',
        department_id=1,
    )


@pytest.fixture
def ticket():
    ticket_create = Ticket.objects.create(
        title='fake_title',
        description='fake_description',
        status='Not Acknowledged',
        priorytet='Low',
        date_creation=timezone.now(),
        date_update=timezone.now(),
        date_resolve=timezone.now(),
        department_assignment_id=1,
        problem_category_id=1,
        user_requestor_id=1,
        # user_assignment_id=1,
    )
    ticket_create.user_assignment.add(1)
    return ticket_create


@pytest.fixture
def correspondence():
    return Correspondence.objects.create(
        user_id=1,
        description='Test Corespondence Description',
        date_creation=timezone.now(),
        ticket_correspondence_id=1,
    )
