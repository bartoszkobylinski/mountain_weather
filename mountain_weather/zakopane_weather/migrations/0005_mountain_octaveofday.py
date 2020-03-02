# Generated by Django 3.0 on 2020-01-11 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zakopane_weather', '0004_auto_20191211_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_peak', models.CharField(max_length=50)),
                ('elevation', models.IntegerField()),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OctaveOfDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('octave_of_a_day', models.CharField(max_length=50)),
                ('wind_speed', models.IntegerField()),
                ('summary', models.CharField(max_length=50)),
                ('rain', models.IntegerField()),
                ('snow', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('chill_temperature', models.IntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakopane_weather.Mountain')),
            ],
        ),
    ]
