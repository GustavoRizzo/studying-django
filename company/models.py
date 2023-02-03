from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200)
    founding_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Member(models.Model):
    fk_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    hiring_date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.name
