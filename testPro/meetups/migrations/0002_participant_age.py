# Generated by Django 4.0 on 2021-12-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='age',
            field=models.IntegerField(default=18, max_length=2),
            preserve_default=False,
        ),
    ]
