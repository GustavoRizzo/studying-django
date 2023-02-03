from django.db import models
from django.utils import timezone
from datetime import date

class Company(models.Model):
    name = models.CharField(max_length=200)
    url_img = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Member(models.Model):
    fk_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    hiring_date = models.DateField(default= date.today)

    def __str__(self):
        return self.name
