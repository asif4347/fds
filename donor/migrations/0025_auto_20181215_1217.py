# Generated by Django 2.1.4 on 2018-12-15 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0024_auto_20181213_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='code',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='gender',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_type',
            field=models.CharField(choices=[('Fast Food', 'Fast Food'), ('Regular Food', 'Regular Food')], max_length=15),
        ),
        migrations.AlterField(
            model_name='food',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 12, 15, 12, 17, 22, 17940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='preparation_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 12, 15, 12, 17, 22, 17876, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Picked', 'Picked'), ('New Entry', 'New Entry')], default='New Entry', max_length=10),
        ),
    ]
