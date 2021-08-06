# Generated by Django 3.2.3 on 2021-07-19 20:51

from django.db import migrations, models
import django.db.models.deletion


def temp_artist_gen(apps, schema_editor):
    Artist = apps.get_model("service_generator", "Artist")
    Song = apps.get_model("service_generator", "Song")

    for song in Song.objects.all():
        artist, created = Artist.objects.get_or_create(name=song.artist)
        song.temp_artist = artist
        song.save()

class Migration(migrations.Migration):

    dependencies = [
        ('service_generator', '0008_auto_20210716_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='temp_artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service_generator.artist'),
        ),
        migrations.RunPython(temp_artist_gen)
    ]