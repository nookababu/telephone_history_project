from django.db import models

class TelephoneHistory(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    number = models.CharField(max_length=20)
