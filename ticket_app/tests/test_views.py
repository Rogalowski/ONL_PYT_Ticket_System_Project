import pytest
from django.urls import reverse
from django.utils import timezone
# from django.test import Client
from ticket_app.models import Ticket, Department, DepartmentProblem, User


@pytest.mark.django_db
def test_department_model(department):
    assert len(Department.objects.all()) >= 1
    assert Department.objects.get(name_department='IT') == department


@pytest.mark.django_db
def test_departmentproblem_model(department_problem):
    assert DepartmentProblem.objects.get(category_problem='Desktops/Software') == department_problem
    assert DepartmentProblem.objects.first()


@pytest.mark.django_db
def test_ticket_model(ticket):
    assert Ticket.objects.get(title='fake_title1') == ticket
    assert len(Ticket.objects.all()) == 1



@pytest.mark.django_db
def test_ticket_user_assignment_model(ticket):
    assert len(Ticket.objects.all()) >= 1
    assert Ticket.objects.all().get(title='fake_title1') == ticket
    assert Ticket.objects.get(user_assignment_id=1) == ticket


@pytest.mark.django_db  # polaczenie z testową baza danych
def test_ticket_list_model(client, department, user, department_problem):  # ,ticket):
    # client = Client() #stworzona fixtura?
    response = client.get(f'/tickets/{department.name_department}/', {
        'title': 'title',
        'description': 'description',
        'status': 'Not Acknowledged',
        'priorytet': 'Low',
        'date_creation': '2021-09-11 06:17:56.543592 +00:00',
        'date_update': '2021-09-11 06:17:56.543592 +00:00',
        'date_resolve': '2021-09-11 06:17:56.543592 +00:00',
        'department_assignment': department,
        'problem_category': department_problem,
        'user_requestor': user,
    })
    # response = client.get(f'/tickets/ALL/', {})
    for name_ctx in [
        'title',
        'description',
        'status',
        'priorytet',
        'date_creation',
        'date_update',
        'date_resolve',
        'department_assignment',
        'problem_category',
        'user_requestor',
        'user_assignment',
    ]:
        assert response.context[name_ctx] == getattr(department, name_ctx)
    assert response.status_code == 200
    assert len(response.context['title']) == 1



        # assert response.context[name_ctx] == getattr(ticket, name_ctx)

    # class Ticket:
    #     title = 'title'
    #     description = 'desc'
    #
    # ticket = Ticket()
    # description = getattr(ticket, 'description', 'title1') => 'title3'


@pytest.mark.django_db
def test_ticket_details(client, ticket):
    response = client.get(f'/ticket/{ticket.id}', {})  #, {'id': '1'}
    # for name_ctx in [
    #     'title',
    #     'description',
    #     'status',
    #     'priorytet',
    #     'date_creation',
    #     'date_update',
    #     'date_resolve',
    #     'department_assignment',
    #     'problem_category',
    #     'user_requestor',
    #     'user_assignment',
    # ]:
    #     assert response.context[name_ctx] == getattr(ticket, name_ctx)
    assert response.status_code == 200  # testujemy, czy strona nas wpuściła?


@pytest.mark.django_db
def test_ticket_edit(user, client, ticket):
    client.login(username='jacek', password='jacek')
    response = client.get(f'/ticket_edit/{ticket.id}')
    assert response.status_code == 200  # testujemy, czy strona nas wpuściła?


@pytest.mark.django_db
def test_ticket_create(user, client, ticket):
    # client = Client()
    # client.force_login(user='jacek')
    client.login(username='jacek', password='jacek')
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


@pytest.mark.django_db
def test_login_model(client):
    response = client.get(reverse('user_login_home'))
    # response = client.get(f'/login_home/')
    assert response.status_code == 200  # testujemy, czy strona nas wpuściła?

@pytest.mark.django_db
def test_user(client, user):
    client.login(username='jacek', password='jacek')
    response = client.post(f'/login_home/', {
        'username': 'jacek',
        'password': 'jacek',
    })
    assert response.status_code == 200  # testujemy, czy strona nas wpuściła?
# @pytest.mark.django_db
# def test_login2(client):
#     client = Client()
#     client.login(username='jacek', password='jacek')
#     response = client.get('', {
#         'username': 'jacek',
#         'password': 'jacek',
#     })
#     assert response.status_code == 200
