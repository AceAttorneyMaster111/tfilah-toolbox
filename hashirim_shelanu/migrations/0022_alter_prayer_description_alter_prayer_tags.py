# Generated by Django 4.2.1 on 2023-06-06 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashirim_shelanu', '0021_song_apple_music_song_spotify_song_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='prayer',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='prayers', to='hashirim_shelanu.prayertag'),
        ),
    ]
