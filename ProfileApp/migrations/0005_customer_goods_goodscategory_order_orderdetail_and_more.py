# Generated by Django 4.1.4 on 2023-02-05 09:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0004_rename_product1_productm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('surname', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('telephone', models.CharField(default='', max_length=10)),
                ('gender', models.CharField(default='', max_length=10)),
                ('carreer', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('gid', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('brand', models.CharField(default='', max_length=30)),
                ('mode', models.CharField(default='', max_length=30)),
                ('price', models.FloatField(default=0.0)),
                ('net', models.IntegerField(default=0)),
                ('property', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gc_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.date(2023, 2, 5))),
                ('status', models.CharField(default='', max_length=50)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.customer')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.order')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='productm',
            name='catagory',
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
        migrations.DeleteModel(
            name='ProductM',
        ),
        migrations.AddField(
            model_name='goods',
            name='goodscategory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.goodscategory'),
        ),
    ]
