# Generated by Django 2.1.4 on 2018-12-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0011_auto_20181213_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='volenteer',
            name='code',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='volenteer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]