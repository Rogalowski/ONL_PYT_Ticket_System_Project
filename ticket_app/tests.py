from django.test import TestCase

# Create your tests here.

from ticket_app.models import Ticket
import pytest

@pytest.mark.test_ticketing_db
def test_ticket_model(ticket):
    assert len(Ticket.objects.all()) == 1
    assert Ticket.objects.get(title='fake_title') == ticket
