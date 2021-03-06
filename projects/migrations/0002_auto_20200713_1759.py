# Generated by Django 2.2.10 on 2020-07-13 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doneprojects',
            name='body',
            field=models.TextField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doneprojects',
            name='project_url',
            field=models.URLField(default='this is default text'),
        ),
        migrations.AlterField(
            model_name='doneprojects',
            name='backend',
            field=models.CharField(default='this is default text', max_length=256),
        ),
    ]
