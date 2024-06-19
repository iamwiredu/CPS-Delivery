# Generated by Django 4.2.6 on 2024-06-16 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0012_deliveryrequest_pickedup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryrequest',
            name='rider',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='assignments', to='delivery.rider'),
        ),
    ]
