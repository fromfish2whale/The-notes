from django.db import models

# Create your models here.
class blank_for_notes(models.Model):
    date = models.DateField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)