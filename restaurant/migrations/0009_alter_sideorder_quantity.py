# Generated by Django 5.0.6 on 2024-10-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_side_sideorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sideorder',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
