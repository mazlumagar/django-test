from django.db import models

# Create your models here.
class Model1(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Model2(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
