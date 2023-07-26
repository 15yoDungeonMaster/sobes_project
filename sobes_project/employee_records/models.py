from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=True, null=False)
    job_title = models.CharField(max_length=100, blank=False, null=False)
    chief = models.ManyToManyField('Employee', blank=True, related_name='employees')

    def __str__(self):
        return f'{self.name} {self.surname} ({self.job_title})'



