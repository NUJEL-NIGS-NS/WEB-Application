# Generated by Django 4.2.1 on 2023-05-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterstates',
            name='Path',
            field=models.CharField(default='AP', max_length=10),
        ),
    ]
