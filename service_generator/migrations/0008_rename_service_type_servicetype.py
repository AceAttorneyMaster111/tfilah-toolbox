# Generated by Django 4.0 on 2022-10-20 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashirim_shelanu', '0018_rename_chordsheet_contributor_chordsheetcontributor_and_more'),
        ('service_generator', '0007_rename_iyun_element_iyunelement_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service_Type',
            new_name='ServiceType',
        ),
    ]