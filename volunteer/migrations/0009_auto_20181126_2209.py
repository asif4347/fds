# Generated by Django 2.1.3 on 2018-11-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0008_auto_20181118_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volenteer',
            name='cnic',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='volenteer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
