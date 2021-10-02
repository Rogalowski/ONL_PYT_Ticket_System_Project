from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.urls import reverse

STATUS = (
    ('Not Acknowledged', 'Not Acknowledged'),
    ('Pending ', 'Pending'),
    ('Pending Requestor Information', 'Pending Requestor Information'),
    ('Work in Progress', 'Work in Progress'),
    ('Blocked', 'Blocked'),
    ('Dropped', 'Dropped'),
    ('Resolved Successfull', 'Resolved Successfull'),
)

PRIORITY = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('ASAP', 'ASAP'),
)

DEPARTMENTS = (
    ('Test', 'Test'),
    ('IT', 'IT'),
    ('HR', 'HR'),
    ('PM', 'PM'),
    ('F&B', 'F&B'),
)

CATEGORY_PROBLEM = (
    ('Desktops/Software', 'Desktops/Software'),
    ('Pherieral devices', 'Pherieral devices'),
    ('Mobile Devices', 'Mobile Devices'),
    ('Network/Infrastructure', 'Network/Infrastructure'),

    ('Work Schedule', 'Work Schedule'),
    ('Hiring Process', 'Hiring Process'),
    ('Employee', 'Employee'),
    ('Documents', 'Documents'),

    ('Project realization', 'Project realization'),
    ('Improvement', 'Improvement'),
    ('Inspection', 'Inspection'),

    ('Invoices', 'Invoices'),
    ('Payment', 'Payment'),
    ('Delegation payment', 'Delegation payment'),
    ('Orders', 'Orders'),

    ('Other', 'Other'),
)


class Department(models.Model):
    name_department = models.CharField(max_length=64)
    desc_department = models.CharField(max_length=255)

    # Add description of object
    def __str__(self):
        return self.name_department


class DepartmentProblem(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category_problem = models.CharField(choices=CATEGORY_PROBLEM, max_length=64)

    # Another description set for object
    def __str__(self):
        self.dept_and_problem = f'{self.department} :: {self.category_problem}'
        return self.dept_and_problem


# User model Inheritanced from Abstract User that have build in commented entries
class User(AbstractUser):
    # username = models.CharField()
    # first_name = models.CharField(_('first name'), max_length=150, blank=True)
    # last_name = models.CharField(_('last name'), max_length=150, blank=True)
    # email = models.EmailField(_('email address'), blank=True)
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField(),
    # date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    address_city = models.CharField(max_length=64, default='N/A')
    phone_number = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='1')

    def __str__(self):
        self.name_and_dept = f'{self.username} from {self.department} Department'
        return self.name_and_dept


# TO DO, should add every date time and description changes of ticket. Each changes.
class HistoryTicket(models.Model):
    description = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)


# Ticket model
class Ticket(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)
    status = models.CharField(choices=STATUS, max_length=64, default='Not Acknowledged')
    priorytet = models.CharField(choices=PRIORITY, max_length=64, default=1)
    date_creation = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True)
    date_resolve = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    department_assignment = models.ForeignKey(Department, on_delete=models.CASCADE)
    problem_category = models.ForeignKey(DepartmentProblem, on_delete=models.CASCADE, default='',
                                         related_name="ticket_problem_category")
    user_requestor = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name="ticket_user_requestor")
    user_assignment = models.ManyToManyField(User)

    def get_absolute_url(self):

        return reverse('ticket', kwargs={'ticket_id': self.id})


# Correspondence model
class Correspondence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    date_creation = models.DateTimeField(auto_now_add=True)
    ticket_correspondence = models.ForeignKey(Ticket, related_name="ticket_correspondence",
                                              on_delete=models.CASCADE, default='')

    def get_absolute_url(self):
        return reverse('ticket', kwargs={'ticket_id': self.pk})
