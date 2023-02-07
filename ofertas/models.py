from django.db import models

# Create your models here.
class Oferta(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    url_img = models.CharField(max_length=500)
    supplier_link = models.CharField(max_length=500)

    def __str__(self):
        return self.name