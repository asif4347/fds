# Generated by Django 2.1.1 on 2018-11-18 16:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0016_auto_20181111_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='cnic',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='gender',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 11, 18, 16, 6, 13, 640634, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='preparation_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 11, 18, 16, 6, 13, 640634, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('New Entry', 'New Entry'), ('Picked', 'Picked')], default='New Entry', max_length=10),
        ),
    ]
