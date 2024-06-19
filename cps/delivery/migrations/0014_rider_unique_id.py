# Generated by Django 4.2.6 on 2024-06-16 22:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0013_alter_deliveryrequest_rider'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
