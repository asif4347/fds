# Generated by Django 2.1.4 on 2018-12-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0010_auto_20181210_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volenteer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True),
        ),
    ]
