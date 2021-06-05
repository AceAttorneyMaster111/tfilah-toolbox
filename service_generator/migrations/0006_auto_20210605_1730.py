# Generated by Django 3.2.3 on 2021-06-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_generator', '0005_auto_20210603_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayer',
            name='included_services',
        ),
        migrations.AddField(
            model_name='service_type',
            name='prayers',
            field=models.ManyToManyField(through='service_generator.Prayer_Position', to='service_generator.Prayer'),
        ),
    ]
