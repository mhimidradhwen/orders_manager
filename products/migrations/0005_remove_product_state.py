# Generated by Django 4.1.4 on 2023-01-05 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='state',
        ),
    ]
