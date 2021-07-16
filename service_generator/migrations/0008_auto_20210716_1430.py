# Generated by Django 3.2.3 on 2021-07-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_generator', '0007_auto_20210715_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chordsheet_Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='chordsheet',
            name='contributor',
        ),
        migrations.AddField(
            model_name='chordsheet',
            name='contributors',
            field=models.ManyToManyField(to='service_generator.Chordsheet_Contributor'),
        ),
    ]