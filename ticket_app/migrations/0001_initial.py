
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('address_city', models.CharField(default='N/A', max_length=64)),
                ('phone_number', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_department', models.CharField(max_length=64)),
                ('desc_department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_problem', models.CharField(choices=[('Desktops/Software', 'Desktops/Software'), ('Pherieral devices', 'Pherieral devices'), ('Mobile Devices', 'Mobile Devices'), ('Network/Infrastructure', 'Network/Infrastructure'), ('Work Schedule', 'Work Schedule'), ('Hiring Process', 'Hiring Process'), ('Employee', 'Employee'), ('Documents', 'Documents'), ('Project realization', 'Project realization'), ('Improvement', 'Improvement'), ('Inspection', 'Inspection'), ('Invoices', 'Invoices'), ('Payment', 'Payment'), ('Delegation payment', 'Delegation payment'), ('Orders', 'Orders'), ('Other', 'Other')], max_length=64)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_app.Department')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('Not Acknowledged', 'Not Acknowledged'), ('Pending ', 'Pending'), ('Pending Requestor Information', 'Pending Requestor Information'), ('Work in Progress', 'Work in Progress'), ('Blocked', 'Blocked'), ('Dropped', 'Dropped'), ('Resolved Successfull', 'Resolved Successfull')], default='Not Acknowledged', max_length=64)),
                ('priorytet', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('ASAP', 'ASAP')], default=1, max_length=64)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_resolve', models.DateTimeField(blank=True, null=True)),
                ('department_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_app.Department')),
                ('problem_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_problem_category', to='ticket_app.DepartmentProblem')),
                ('user_assignment', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('user_requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_user_requestor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('ticket_correspondence', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_correspondence', to='ticket_app.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='ticket_app.Department'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
