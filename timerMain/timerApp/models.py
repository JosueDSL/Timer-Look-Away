from django.contrib.auth.models import User
from django.db import models

class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="timers")
    name = models.CharField(max_length=64)
    interval = models.IntegerField()
    message = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return f"Name: {self.name} # Interval: {self.interval} # Date: {self.date}"