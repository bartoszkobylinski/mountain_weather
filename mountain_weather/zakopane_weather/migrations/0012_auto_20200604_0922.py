# Generated by Django 3.0 on 2020-06-04 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zakopane_weather', '0011_auto_20200604_0803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peakforecast',
            old_name='name',
            new_name='name_of_peak',
        ),
    ]