# Generated by Django 3.2.3 on 2021-05-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashirim_shelanu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_type',
            name='prayers',
        ),
        migrations.AddField(
            model_name='prayer',
            name='included_services',
            field=models.ManyToManyField(through='hashirim_shelanu.Prayer_Position', to='hashirim_shelanu.Service_Type'),
        ),
        migrations.AddField(
            model_name='song',
            name='chordsheet',
            field=models.FileField(default=b'', upload_to='chordsheets/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='release_year',
            field=models.PositiveSmallIntegerField(blank=True, default=2000),
            preserve_default=False,
        ),
    ]
