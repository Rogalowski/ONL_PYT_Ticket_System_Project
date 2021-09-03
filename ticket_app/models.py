from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser

STATUS = (
    ('Not Acknowledged', 'Not Acknowledged'),
    ('Pending', 'Pending'),
    ('Work in Progress', 'Work in Progress'),
    ('Resolved', 'Resolved'),
)

STATUS_REASON = (
    ('Schedule', 'Schedule'),
    ('Requestor Information,', 'Requestor Information'),
    ('Successfull', 'Successfull'),
    ('Not Successfull', 'Not Successfull'),
)

PRIORITY = (
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
    (4, 'ASAP'),
)

DEPARTMENTS = (
    ('IT', 'IT'),
    ('HR', 'HR'),
    ('PM', 'PM'),
    ('F&B', 'F&B'),
)

CATEGORY_PROBLEM = (
    ('Desktops/laptops', 'Desktops/laptops'),
    ('Pherieral devices', 'Pherieral devices'),
    ('Mobile Devices', 'Mobile Devices'),
    ('Network Infrastructure', 'Network Infrastructure'),

    ('Work Schedule', 'Work Schedule'),
    ('Hiring Process', 'Hiring Process'),
    ('Employee', 'Employee'),
    ('Documents', 'Documents'),

    ('Project realization', 'Project realization'),
    ('Improvement', 'Improvement'),
    ('Inspection', 'Inspection'),
    ('Desktops/laptops', 'Desktops/laptops'),

    ('Invoices', 'Invoices'),
    ('Payment', 'Payment'),
    ('Delegation payment', 'Delegation payment'),
    ('Orders', 'Orders'),

    ('Other', 'Other'),
)
class StatusState(models.Model):
    name_reason_stat = models.CharField(max_length=64)
    # name_reason_stat = models.CharField(choices=REASON, max_length=64)


class Status(models.Model):
    name_status = models.CharField(choices=STATUS, max_length=64)
    status_statement = models.OneToOneField(StatusState, on_delete=models.CASCADE)


class Department(models.Model):
    name_department = models.CharField(choices=DEPARTMENTS, max_length=64)
    desc_department = models.CharField(max_length=255)
    # category_problem = models.CharField(choices=DEPT_PROBLEM, max_length=255)


class DepartmentProblem(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    category_problem = models.CharField(choices=CATEGORY_PROBLEM, max_length=64)
    # type_dept_problem = models.OneToOneField(TypeDeptProblem) #opcjonalnie kiedys


# class TypeDeptProblem(models.Model): #opcjonalnie kiedys
#     name_problem = models.CharField(choices=TYPE_PROBLEM, max_length=64)
#     name_problem = models.OneToOneField(DepartmentProblems)


class User(AbstractUser, PermissionsMixin):
    # username = models.CharField()
    # first_name = models.CharField(_('first name'), max_length=150, blank=True)
    # last_name = models.CharField(_('last name'), max_length=150, blank=True)
    # email = models.EmailField(_('email address'), blank=True)
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField(),
    # date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    address_city = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    department = models.OneToOneField(Department, on_delete=models.CASCADE)

class Correspondence(models.Model):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)  # CZY MOZE USER?
    description = models.CharField(max_length=1000)
    date_creation = models.DateTimeField(auto_now_add=True)

class HistoryTicket(models.Model):
    description = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    # status = models.CharField(choices=STATUS, default='Not Acknowledged')
    status = models.OneToOneField(Status, on_delete=models.CASCADE, default='Not Acknowledged')
    # status_state?
    priorytet = models.CharField(choices=PRIORITY, max_length=64, default=1)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_resolve = models.DateTimeField(auto_now_add=True)
    correspondence = models.ManyToManyField(Correspondence)  # ''?
    department_assignment = models.OneToOneField(Department, on_delete=models.CASCADE)
    problem_problem_category = models.OneToOneField(DepartmentProblem, on_delete=models.CASCADE)
    user_requestor = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)  # CZY MOZE USER? #cały dział czy osoby lub osoba
    file_path = models.FilePathField()
    history_tt = models.ManyToManyField(HistoryTicket, on_delete=models.CASCADE)  # osobna tabela do tego? ma zbierac zmiany w tt typu status, korespondencja, categoria przez kogo zostala utworzona zmiana




