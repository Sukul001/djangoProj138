# Generated by Django 4.1.4 on 2023-02-16 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0022_remove_goods_goodscategory_remove_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sme',
            name='customerid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ProfileApp.customers'),
        ),
    ]
