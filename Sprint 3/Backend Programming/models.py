from django.db import models

# Create your models here.

class Donation(models.Model):
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=False, max_length=30)
    email = models.CharField(max_length=30)
    date = models.DateField()
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return self.email