# Generated by Django 4.2.1 on 2023-05-18 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AP', '0004_ap_geolocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_data_ap',
            name='financial_year',
            field=models.IntegerField(default=2022),
        ),
    ]
