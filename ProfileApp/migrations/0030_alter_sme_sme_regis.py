# Generated by Django 4.1.4 on 2023-02-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0029_rename_cid_sme_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sme',
            name='sme_regis',
            field=models.DateField(default=None),
        ),
    ]
