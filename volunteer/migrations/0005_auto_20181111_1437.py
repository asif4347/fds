# Generated by Django 2.1.3 on 2018-11-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_auto_20181111_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='volenteer',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='volenteer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Other', 'Other'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
