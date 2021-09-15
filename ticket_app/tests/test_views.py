import pytest
from django.test import Client
from ticket_app.models import Ticket, Department


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
def test_ticket_model(ticket):
    assert len(Ticket.objects.all()) == 1
    assert Ticket.objects.get(title='fake_title') == ticket


@pytest.mark.django_db  # polaczenie z testową baza danych
def test_ticket_detail(client, ticket):
    response = client.get(f'/tickets/ALL/')
    # response = client.get(f'/ticket/{ticket.pk}/')
    assert response.status_code == 200
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
        assert response.context[name_ctx] == getattr(ticket, name_ctx)