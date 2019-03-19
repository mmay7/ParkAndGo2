# Generated by Django 2.1.7 on 2019-03-19 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ticket_number', models.IntegerField()),
                ('meter_number', models.IntegerField()),
                ('street', models.CharField(max_length=200)),
                ('date_and_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
