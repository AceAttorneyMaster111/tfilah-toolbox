# Generated by Django 3.2.3 on 2021-08-10 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashirim_shelanu', '0013_auto_20210810_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_type',
            name='prayers',
        ),
        migrations.DeleteModel(
            name='Prayer_Position',
        ),
        migrations.DeleteModel(
            name='Service_Type',
        ),
    ]
