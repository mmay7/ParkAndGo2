# Generated by Django 2.1.7 on 2019-05-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_auto_20190514_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
    ]
