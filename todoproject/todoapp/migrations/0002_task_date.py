# Generated by Django 3.2.3 on 2021-07-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=1997),
            preserve_default=False,
        ),
    ]
