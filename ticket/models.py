from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ticKet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_number = models.IntegerField()
    meter_number = models.IntegerField()
    street = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    weekday = models.IntegerField()

    def create_ticket(self):
        self.date_and_time = timezone.now()
        self.save()

    def __repr__(self):
        return repr(self.ticket_number)


class search(models.Model):
    weekday_word = models.CharField(max_length=200)
    weekday_num = models.IntegerField()
    meter_number = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def create_search(self):
        self.save()

    def __repr__(self):
        return repr(self.meter_number)
