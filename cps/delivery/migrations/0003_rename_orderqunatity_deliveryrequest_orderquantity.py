# Generated by Django 4.2.6 on 2024-06-07 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0002_rename_sendernumner_deliveryrequest_sendernumber"),
    ]

    operations = [
        migrations.RenameField(
            model_name="deliveryrequest",
            old_name="orderQunatity",
            new_name="orderQuantity",
        ),
    ]
