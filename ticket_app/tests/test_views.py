import pytest
from django.test import Client
from django.utils import timezone

from ticket_app.models import Ticket, Department, DepartmentProblem


# client = Client()
# response = client.get('', {
#     'username': 'jacek',
#     'password': 'jacek',
# })
# response.status_code


@pytest.mark.django_db
def test_department_model(department):
    assert len(Department.objects.all()) == 1
    assert Department.objects.get(name_department='IT') == department


@pytest.mark.django_db
def test_department_problem_model(department_problem):
    assert DepartmentProblem.objects.first()
    assert DepartmentProblem.objects.get(category_problem='Desktops/Software') == department_problem


@pytest.mark.django_db
def test_ticket_model(ticket):
    assert len(Ticket.objects.all()) == 1


@pytest.mark.django_db
def test_ticket_user_assignment_model(ticket):
    assert len(Ticket.objects.all()) == 1
    assert Ticket.objects.all().get(title='fake_title2') == ticket
    assert Ticket.objects.get(user_assignment_id=1) == ticket


@pytest.mark.django_db  # polaczenie z testową baza danych
def test_ticket_detail(client, department):  # ,ticket):
    response = client.get(f'/tickets/{department}/')
    # response = client.get(f'/ticket/{ticket.id}/')
    assert response.status_code == 200
    for name_ctx in [
        'title',
        'description',
        'status',
        'priorytet',
        'date_creation',
        'date_update',
        'date_resolve',
        'department_assignment_id',
        'problem_category_id',
        'user_requestor_id',
    ]:
        assert response.context[name_ctx] == getattr(department, name_ctx)
        # assert response.context[name_ctx] == getattr(ticket, name_ctx)

    # class Ticket:
    #     title = 'title'
    #     description = 'desc'
    #
    # ticket = Ticket()
    # description = getattr(ticket, 'description', 'title1') => 'title3'


@pytest.mark.django_db
def test_ticket_detail(client):
    response = client.get(f'/login_home/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_ticket_create(client):
    data = {
        'title': 'created_title',
        'description': 'created_description',
        'status': 'Not Acknowledged',
        'priorytet': 'Low',
        'date_creation': timezone.now(),
        'date_update': timezone.now(),
        'date_resolve': timezone.now(),
        'department_assignment_id': 1,
        'problem_category_id': 1,
        'ticket_user_requestor': 1,
        'user_assignment': 1,
    }
    response = client.post(f'/create_ticket/', data)
    assert response.status_code == 302
    assert Ticket.objects.first().title == 'created_title'
