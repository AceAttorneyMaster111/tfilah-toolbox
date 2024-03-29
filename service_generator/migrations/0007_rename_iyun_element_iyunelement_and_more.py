# Generated by Django 4.0 on 2022-10-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashirim_shelanu', '0018_rename_chordsheet_contributor_chordsheetcontributor_and_more'),
        ('service_generator', '0006_remove_service_element_list_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Iyun_Element',
            new_name='IyunElement',
        ),
        migrations.RenameModel(
            old_name='Other_Element',
            new_name='OtherElement',
        ),
        migrations.RenameModel(
            old_name='Prayer_Position',
            new_name='PrayerPosition',
        ),
        migrations.RenameModel(
            old_name='Reading_Element',
            new_name='ReadingElement',
        ),
        migrations.DeleteModel(
            name='Prayer_Element',
        ),
        migrations.DeleteModel(
            name='Song_Element',
        ),
        migrations.CreateModel(
            name='PrayerElement',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hashirim_shelanu.prayer', models.Model),
        ),
        migrations.CreateModel(
            name='SongElement',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hashirim_shelanu.song', models.Model),
        ),
    ]
