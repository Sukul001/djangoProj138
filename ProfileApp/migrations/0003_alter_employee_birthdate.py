# Generated by Django 4.1.4 on 2023-02-05 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birthdate',
            field=models.DateTimeField(default=datetime.date(2023, 2, 5)),
        ),
    ]