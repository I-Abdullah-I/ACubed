# Generated by Django 2.2.10 on 2020-07-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_feedbacks_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='name',
            field=models.CharField(default='name', max_length=254),
        ),
    ]
