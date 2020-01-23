from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=20)
    employer = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=20, null=True)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)