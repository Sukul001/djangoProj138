# Generated by Django 4.1.4 on 2023-02-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0005_customer_goods_goodscategory_order_orderdetail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
    ]
