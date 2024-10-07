# Generated by Django 5.0.6 on 2024-10-07 05:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_remove_food_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]