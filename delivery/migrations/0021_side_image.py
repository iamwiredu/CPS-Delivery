# Generated by Django 5.0.6 on 2024-10-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0020_side_sideorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='side',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/sides'),
        ),
    ]