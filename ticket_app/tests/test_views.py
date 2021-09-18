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
def test_ticket_user_assignment_model(ticket, user, ticket_user_assignment):
    assert len(Ticket.objects.all()) >= 1
    assert Ticket.objects.all().get(title='fake_title1') == ticket
    assert Ticket.objects.get(user_requestor=user) == ticket
    assert Ticket.objects.get(user_assignment=ticket_user_assignment) == ticket_user_assignment



@pytest.mark.django_db
def test_ticket_create(user, client, ticket, department, department_problem):
    # client = Client()
    # client.force_login(user='jacek')
    # client.login(username='jacek', password='jacek')

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
    # assert Ticket.objects.first().title == 'created_title'


# @pytest.mark.django_db
# def test_login_model(client):
#     response = client.get(reverse('user_login_home'))
#     # response = client.get(f'/login_home/')
#     assert response.status_code == 200  # testujemy, czy strona nas wpuściła?
#

@pytest.mark.django_db
def test_user(client, user):
    # client.login(username=user.username, password=user.password)
    response = client.post(f'/login_home/', {
        'username': user.username,
        'password': user.password,
    })
    assert response.status_code == 200  # testujemy, czy strona nas wpuściła?
    assert user.username == 'jacek'


@pytest.mark.django_db  # polaczenie z testową baza danych
def test_ticket_list_model(client, ticket, department, user, department_problem):  # ,ticket):
    # client = Client() #stworzona fixtura?
    breakpoint()
    response = client.get(f'/tickets/ALL/')
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
def test_ticket_details(client, ticket, user):
    # client.force_login(user=user)

    response = client.get(f'/ticket/{ticket.id}/', {})  #, {'id': '1'}
    # assert response.status_code == 200
    # assert len(response.context['title']) == 1
    breakpoint()
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
        # 'user_assignment',
    ):
        assert field in response.data



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
    #     # 'user_assignment',
    # ]:
    #     print(f'AAAAAAAAAAAAAAA {name_ctx}')
    #     assert response.context[name_ctx] == getattr(ticket, name_ctx)





@pytest.mark.django_db
def test_ticket_edit(user, client, ticket):
    client.login(username='jacek', password='jacek')
    response = client.get(f'/ticket_edit/{ticket.id}')
    assert response.status_code == 200  # testujemy, czy strona nas wpuściła?


# @pytest.mark.django_db
# def test_update_movie(client, set_up):
#     movie = Movie.objects.first()
#     response = client.get(f"/movies/{movie.id}/", {}, format='json')
#     movie_data = response.data
#     new_year = 3
#     movie_data["year"] = new_year
#     new_actors = [random_person().name]
#     movie_data["actors"] = new_actors
#     response = client.patch(f"/movies/{movie.id}/", movie_data, format='json')
#     assert response.status_code == 200
#     movie_obj = Movie.objects.get(id=movie.id)
#     assert movie_obj.year == new_year
#     db_actor_names = [actor.name for actor in movie_obj.actors.all()]
#     assert len(db_actor_names) == len(new_actors)