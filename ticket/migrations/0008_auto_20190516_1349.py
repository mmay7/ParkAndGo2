# Generated by Django 2.1.7 on 2019-05-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_ticket_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='weekday_word',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Monday', max_length=10),
        ),
    ]
