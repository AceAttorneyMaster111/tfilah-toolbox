# Generated by Django 3.2.3 on 2021-08-11 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_generator', '0003_auto_20210810_2333'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='element_position',
            name='element_unique_index',
        ),
        migrations.RemoveConstraint(
            model_name='prayer_position',
            name='prayer_unique_index',
        ),
        migrations.AlterField(
            model_name='element_position',
            name='index',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
