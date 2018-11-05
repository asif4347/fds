# Generated by Django 2.1.1 on 2018-11-04 14:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0006_auto_20181104_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='food',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 11, 4, 14, 12, 28, 173757, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='preparation_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 11, 4, 14, 12, 28, 173757, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Picked', 'Picked'), ('New Entry', 'New Entry')], default='New Entry', max_length=10),
        ),
    ]