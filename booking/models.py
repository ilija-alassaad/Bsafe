# models.py
from django.db import models


class Administrator(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AvailableTime(models.Model):
    administrator = models.ForeignKey(
        Administrator, related_name='available_times', on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.administrator.name} at {self.time}"


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    available_time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} with {self.administrator} at {self.available_time.time}"
