# Generated by Django 5.0.6 on 2025-03-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0040_alter_bulkdeliverypoint_deliverypoint_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkdeliveryrequest',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
    ]
