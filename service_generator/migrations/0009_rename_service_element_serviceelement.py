# Generated by Django 4.0 on 2022-10-24 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('service_generator', '0008_rename_service_type_servicetype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service_Element',
            new_name='ServiceElement',
        ),
    ]
