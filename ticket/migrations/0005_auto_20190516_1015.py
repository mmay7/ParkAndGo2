# Generated by Django 2.1.7 on 2019-05-16 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='meter',
            new_name='meter_number',
        ),
    ]