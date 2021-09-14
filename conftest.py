import pytest
from django.utils import timezone

from ticket_app.models import Ticket


@pytest.fixture
def ticket():
    return Ticket.objects.create(

        title='fake_title',
        description='fake_description',
        status='Not Acknowledged',
        priorytet='Low',
        date_creation=timezone.now(),
        date_update=timezone.now(),
        date_resolve=timezone.now(),
        department_assignment='IT',
        problem_category='Desktops/Software',
        user_requestor=1,
        user_assignment=2,
    )
