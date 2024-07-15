# Generated by Django 4.2.6 on 2024-06-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_remove_deliveryrequest_rider'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryrequest',
            name='rider',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='delivery.rider'),
        ),
    ]