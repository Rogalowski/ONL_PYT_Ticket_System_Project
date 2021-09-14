import pytest
from django.test import Client


# client = Client()
# response = client.get('', {
#     'username': 'jacek',
#     'password': 'jacek',
# })
# response.status_code


@pytest.mark.django_db
def test_product_detail(client, ticket):
    response = client.get(f'/ticket/{ticket.pk}/')
    assert response.status_code == 200
    for name_ctx in ['title', 'description', 'status']:
        assert response.context[name_ctx] == getattr(ticket, name_ctx)
