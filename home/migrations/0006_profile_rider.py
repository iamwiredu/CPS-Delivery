# Generated by Django 5.0.6 on 2024-09-23 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_bulkdeliverypoint_orderquantity_and_more'),
        ('home', '0005_profile_accounttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rider',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.rider'),
        ),
    ]
