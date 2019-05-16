from django.db import models
from django.contrib.auth.models import User


class proFile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        unique=True,
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    home_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def create_profile(self):
        self.save()

    def __repr__(self):
        return repr(self.first_name)
