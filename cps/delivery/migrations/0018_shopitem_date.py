# Generated by Django 4.2.6 on 2024-06-19 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0017_shopitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
