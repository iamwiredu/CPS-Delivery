# Generated by Django 5.0.6 on 2024-09-21 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_remove_bulkdeliverypoint_deliveryarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkdeliveryrequest',
            name='product',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='deliveryrequest',
            name='product',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bulkdeliveryrequest',
            name='pickupPoint',
            field=models.CharField(choices=[('Kumasi', 'Kumasi')], default='Kumasi', max_length=10),
        ),
        migrations.AlterField(
            model_name='deliveryrequest',
            name='deliveryPoint',
            field=models.CharField(choices=[('Kumasi', 'Kumasi'), ('Cape Coast', 'Cape Coast'), ('Takoradi', 'Takoradi'), ('Koforidua', 'Koforidua'), ('Ho', 'Ho'), ('Sunyani', 'Sunyani'), ('Tarkwa', 'Tarkwa'), ('Obuasi', 'Obuasi'), ('Akosombo', 'Akosombo'), ('Techiman', 'Techiman'), ('Nsawam', 'Nsawam'), ('Nkwakaw', 'Nkwakaw'), ('Winneba', 'Winneba'), ('Mankessim', 'Mankessim'), ('Suhum', 'Suhum'), ('Konongo', 'Konongo')], default='Kumasi', max_length=10),
        ),
        migrations.AlterField(
            model_name='deliveryrequest',
            name='pickupPoint',
            field=models.CharField(choices=[('Kumasi', 'Kumasi')], default='Kumasi', max_length=10),
        ),
    ]
