# Generated by Django 5.0.6 on 2024-10-08 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_alter_sideorder_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sideorder',
            name='side',
        ),
        migrations.DeleteModel(
            name='Side',
        ),
        migrations.DeleteModel(
            name='sideOrder',
        ),
    ]