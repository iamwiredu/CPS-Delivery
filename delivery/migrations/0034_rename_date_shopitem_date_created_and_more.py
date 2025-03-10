# Generated by Django 5.0.6 on 2025-03-10 14:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0033_qrident'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopitem',
            old_name='date',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='deliveryFee',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bulkdeliveryrequest',
            name='product',
            field=models.CharField(blank=True, choices=[('Food', 'Food'), ('item', 'item')], default='item', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryrequest',
            name='product',
            field=models.CharField(blank=True, choices=[('Food', 'Food'), ('item', 'item')], default='item', max_length=255, null=True),
        ),
    ]
