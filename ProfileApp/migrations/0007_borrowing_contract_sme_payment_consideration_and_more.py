# Generated by Django 4.1.4 on 2023-02-11 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0006_alter_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrow_id', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('borrow_date', models.CharField(default='', max_length=20)),
                ('borrow_type', models.CharField(default='', max_length=20)),
                ('borrow_objective', models.CharField(default='', max_length=100)),
                ('borrow_limitmoney', models.FloatField(default=0.0)),
                ('borrow_file', models.CharField(default='', max_length=50)),
                ('borrow_status', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('ct_id', models.CharField(default='', max_length=4, primary_key=True, serialize=False)),
                ('ct_datecontract', models.CharField(default='', max_length=20)),
                ('ct_fine', models.FloatField(default=0.0)),
                ('ct_status', models.CharField(default='', max_length=20)),
                ('ct_payment', models.FloatField(default=0.0)),
                ('ct_interest', models.FloatField(default=0.0)),
                ('ct_amount', models.IntegerField(default=0)),
                ('ct_datepayment', models.CharField(default='', max_length=20)),
                ('ct_dept', models.FloatField(default=0.0)),
                ('ct_limit', models.FloatField(default=0.0)),
                ('br_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.borrowing')),
            ],
        ),
        migrations.CreateModel(
            name='Sme',
            fields=[
                ('sme_id', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('sme_name', models.CharField(default='', max_length=50)),
                ('sme_address', models.CharField(default='', max_length=100)),
                ('sme_zipcode', models.CharField(default='', max_length=5)),
                ('sme_regis', models.CharField(default='', max_length=20)),
                ('sme_history', models.CharField(default='', max_length=100)),
                ('sme_phone', models.CharField(default='', max_length=10)),
                ('sme_agent', models.CharField(default='', max_length=50)),
                ('sme_objective', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pm_id', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('pm_fine', models.FloatField(default=0.0)),
                ('pm_status', models.CharField(default='', max_length=20)),
                ('pm_file', models.CharField(default='', max_length=50)),
                ('pm_bank', models.CharField(default='', max_length=50)),
                ('pm_tranfernumber', models.CharField(default='', max_length=15)),
                ('pm_payment', models.FloatField(default=0.0)),
                ('pm_installment', models.IntegerField(default=0)),
                ('pm_datepayment', models.CharField(default='', max_length=20)),
                ('ct_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Consideration',
            fields=[
                ('csd_id', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('csd_date', models.CharField(default='', max_length=20)),
                ('br_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.borrowing')),
            ],
        ),
        migrations.AddField(
            model_name='borrowing',
            name='sme_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.sme'),
        ),
    ]
