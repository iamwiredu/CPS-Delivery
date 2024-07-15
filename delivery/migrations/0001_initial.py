# Generated by Django 4.2.6 on 2024-06-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeliveryRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("orderQunatity", models.PositiveIntegerField()),
                ("pickupNumber", models.PositiveIntegerField()),
                (
                    "deliveryPoint",
                    models.CharField(
                        choices=[
                            ("Select", "Select"),
                            ("Kumasi", "Kumasi"),
                            ("Cape Coast", "Cape Coast"),
                            ("Takoradi", "Takoradi"),
                            ("Kotoridua", "Kotoridua"),
                            ("Ho", "Ho"),
                            ("Sunyani", "Sunyani"),
                            ("Tarkwa", "Tarkwa"),
                            ("Obuasi", "Obuasi"),
                            ("Akosombo", "Akosombo"),
                            ("Techiman", "Techiman"),
                            ("Nsawam", "Nsawam"),
                            ("Nkwakaw", "Nkwakaw"),
                            ("Winneba", "Winneba"),
                            ("Mankessim", "Mankessim"),
                            ("Suhum", "Suhum"),
                            ("Konongo", "Konongo"),
                        ],
                        default="Select",
                        max_length=10,
                    ),
                ),
                ("dropoffNumber", models.PositiveIntegerField()),
                (
                    "pickupPoint",
                    models.CharField(
                        choices=[
                            ("Select", "Select"),
                            ("Kumasi", "Kumasi"),
                            ("Cape Coast", "Cape Coast"),
                            ("Takoradi", "Takoradi"),
                            ("Kotoridua", "Kotoridua"),
                            ("Ho", "Ho"),
                            ("Sunyani", "Sunyani"),
                            ("Tarkwa", "Tarkwa"),
                            ("Obuasi", "Obuasi"),
                            ("Akosombo", "Akosombo"),
                            ("Techiman", "Techiman"),
                            ("Nsawam", "Nsawam"),
                            ("Nkwakaw", "Nkwakaw"),
                            ("Winneba", "Winneba"),
                            ("Mankessim", "Mankessim"),
                            ("Suhum", "Suhum"),
                            ("Konongo", "Konongo"),
                        ],
                        default="Select",
                        max_length=10,
                    ),
                ),
                ("senderNumner", models.PositiveIntegerField()),
                ("productFee", models.FloatField()),
                ("additionalInfo", models.TextField()),
            ],
        ),
    ]