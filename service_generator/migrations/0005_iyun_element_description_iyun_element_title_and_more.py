# Generated by Django 4.0 on 2022-07-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_generator', '0004_auto_20210810_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='iyun_element',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='iyun_element',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='other_element',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='other_element',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reading_element',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='reading_element',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reading_element',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service_element',
            name='point',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service_type',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
