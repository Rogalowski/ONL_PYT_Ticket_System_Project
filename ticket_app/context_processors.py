
#CONTEXT PROCESSOR
from ticket_app.models import Ticket


def static_tickets(request):
    logged_user = request.user.username
    return {
        'current_user_req_tickets': Ticket.objects.filter(user_requestor__username=logged_user),
        'current_user_tickets': Ticket.objects.filter(user_assignment__username=logged_user),
        'request': request
    }