# Generated by Django 5.0.1 on 2024-01-12 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_quantity',
        ),
    ]
