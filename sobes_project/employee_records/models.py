from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=True, null=False)
    job_title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f'{self.name} {self.surname} | {self.job_title}'


class Subordination(models.Model):
    person = models.OneToOneField(Person, blank=False, null=False, on_delete=models.CASCADE)
    # job_title = models.CharField(max_length=100, blank=False, null=False)
    employee = models.ManyToManyField(Person, blank=True, related_name='chiefs')

    def __str__(self):
        return f'{self.person.name} | {self.person.job_title}'
