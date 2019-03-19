from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=200)
    ticket_number = models.IntegerField()
    meter_number = models.IntegerField()
    street = models.CharField(max_length=200)
    date_and_time = models.DateTimeField(default=timezone.now)

    def create_ticket(self):
        self.date_and_time = timezone.now()
        self.save()

    def __repr__(self):
        return repr(self.ticket_number)
