# Generated by Django 5.0.6 on 2024-09-20 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_rename_pickuppoint_bulkdeliverypoint_deliveryarea_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulkdeliverypoint',
            name='deliveryArea',
        ),
    ]
