# Generated by Django 5.0.6 on 2024-10-08 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0017_alter_cartrestaurant_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryrequest',
            name='product',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
