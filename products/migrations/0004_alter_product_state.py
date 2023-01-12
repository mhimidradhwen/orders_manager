# Generated by Django 4.1.4 on 2023-01-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(choices=[('success', 'Delivred'), ('danger', 'Canceled'), ('warning', 'Wait for confirmation'), ('primary', 'Out for delivery')], default='warning', max_length=50),
        ),
    ]