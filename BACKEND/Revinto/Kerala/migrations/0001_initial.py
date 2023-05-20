# Generated by Django 4.2.1 on 2023-05-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KL_geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Head_quarters', models.CharField(max_length=30)),
                ('Place', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('P_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('P_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('C_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('C_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('H_lat', models.DecimalField(decimal_places=7, max_digits=10)),
                ('H_lon', models.DecimalField(decimal_places=7, max_digits=10)),
                ('Type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='sales_data_KL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True)),
                ('Region', models.CharField(max_length=30)),
                ('Regional_manager', models.CharField(max_length=30)),
                ('Head_quarter', models.CharField(max_length=30)),
                ('Business_executive', models.CharField(max_length=30)),
                ('Agency', models.CharField(max_length=200)),
                ('Product', models.CharField(max_length=60)),
                ('Billed_qty', models.IntegerField()),
                ('Billed_rate', models.DecimalField(decimal_places=2, max_digits=100)),
                ('Company_value', models.DecimalField(decimal_places=2, max_digits=100)),
                ('financial_year', models.IntegerField(default=2022)),
            ],
        ),
    ]
