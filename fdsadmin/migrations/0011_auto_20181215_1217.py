# Generated by Django 2.1.4 on 2018-12-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdsadmin', '0010_auto_20181213_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fdsadmin',
            name='gender',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
