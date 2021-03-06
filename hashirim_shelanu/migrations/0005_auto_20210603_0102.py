# Generated by Django 3.2.3 on 2021-06-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashirim_shelanu', '0004_auto_20210526_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service_type',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='release_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
