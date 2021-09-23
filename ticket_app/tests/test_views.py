import pytest
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from django.utils import timezone
# from django.test import Client
from ticket_app.forms import TicketUpdateForm
from ticket_app.models import Ticket, Department, DepartmentProblem, User, Correspondence
from ticket_app.views import TicketView


@pytest.mark.django_db
def test_department_model(department):
    assert len(Department.objects.all()) >= 1
    assert Department.objects.get(name_department='IT') == department


@pytest.mark.django_db
def test_correspondence_model(ticket, correspondence):
    assert Correspondence.objects.get(description='Test Corespondence Description') == correspondence


@pytest.mark.django_db
def test_departmentproblem_model(department_problem):
    assert DepartmentProblem.objects.get(category_problem='Desktops/Software') == department_problem
    assert DepartmentProblem.objects.first()


@pytest.mark.django_db
def test_ticket_model(ticket):
    assert Ticket.objects.get(title='fake_title1') == ticket
    assert len(Ticket.objects.all()) == 1


@pytest.mark.django_db
def test_ticket_user_assignment_model(ticket, user, ticket_user_assignment):
    assert len(Ticket.objects.all()) >= 1
    assert Ticket.objects.all().get(title='fake_title1') == ticket
    assert Ticket.objects.get(user_requestor=user) == ticket
    assert Ticket.objects.get(user_assignment=user).id == ticket.id


@pytest.mark.django_db
def test_user(client, user, ticket):
    # client.login(username=user.username, password=user.password)
    response = client.post(f'/login_home/', {
        'username': user.username,
        'password': user.password,
    })
    assert response.status_code == 200  # testujemy, czy strona nas wpuściła
    assert response.wsgi_request.user  # <WSGIRequest: POST '/login_home/'>
    assert user.is_authenticated == True  # The same as above?


@pytest.mark.django_db  # polaczenie z testową baza danych
def test_ticket_list_ALL(client, ticket, department):  # ,ticket):
    response = client.get(f'/tickets/ALL/')
    assert Ticket.objects.count() >= 1
    assert response.status_code == 200
    for field in (
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
    ):
        assert response.context['tickets'], field == getattr(ticket, field)


@pytest.mark.django_db  # polaczenie z testową baza danych
def test_ticket_list_department(client, ticket, department):  # ,ticket):
    response = client.get(f'/tickets/{department}/', {})
    # response = client.get(f'/tickets/IT/')
    assert Ticket.objects.count() >= 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_ticket_details(client, ticket, correspondence):
    # client.force_login(user=user)
    response = client.get(reverse('ticket', args=[ticket.id]))
    assert response.status_code == 200
    for field in (
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
            'ticket_correspondence',
            'user_assignment',
    ):
        assert response.resolver_match.func.__name__, TicketView.as_view().__name__  # Verify the view that served the response
        assert Ticket.objects.count() >= 1
        assert getattr(response.context['ticket'], field) == getattr(ticket, field)


@pytest.mark.django_db
def test_ticket_create(user, client, ticket, department, department_problem):
    ticket_before = Ticket.objects.count()
    data = {
        'title': 'created_title',
        'description': 'created_description',
        'status': 'Not Acknowledged',
        'priorytet': 'Low',
        'date_creation': timezone.now(),
        'date_update': timezone.now(),
        'date_resolve': timezone.now(),
        'department_assignment': department.id,
        'problem_category': department_problem.id,
        'user_requestor': user.id,
        'user_assignment': user.id,
    }
    client.force_login(user=user)
    response = client.post(f'/create_ticket/', data)

    assert response.status_code == 302
    assert Ticket.objects.get(title='created_title')
    assert Ticket.objects.count() == ticket_before + 1
    # assert Ticket.objects.first().title == 'created_title'




@pytest.mark.django_db
def test_ticket_edit(client, ticket, user, department, department_problem, correspondence):
    # client.login(username='jacek', password='jacek')
    client.force_login(user=user)
    response = client.get(reverse('ticket_edit', args=[ticket.id]))
    assert response.status_code == 200
    # response = client.get(f"/ticket/{ticket.id}/", {})
    # breakpoint()
    tt = response
    # ticket.title = 'New_TITLE'
    tt['title'] = 'New_TITLE'

    response = client.post(f"/ticket_edit/{ticket.id}/", tt)
    assert response.status_code == 200
    ticket.refresh_from_db()
    tt.refresh_from_db()
    breakpoint()

    # assert response_edit.status_code == 200
    assert Ticket.objects.get(title='New_TITLE')
    # ticket_obj = Ticket.objects.get(id=ticket.id)
    # assert ticket_obj.title == 'Edited_Title'
    # db_ticket_names = [ticket.title for ticket in ticket_obj.ticket.all()]
    # assert len(db_ticket_names) == len(ticket_data)

    #
    # data = {
    #     'title': 'created_title',
    #
    # client.force_login(user=user)
    # response = client.post(f'/create_ticket/', data)
