# Generated by Django 3.2.7 on 2021-09-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0019_alter_user_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_resolve',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
