from django.db import models

class Course(models.Model):
    crn = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)
    meeting_time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    seating_availability = models.CharField(max_length=200)
    waitlist_availability = models.CharField(max_length=200)
