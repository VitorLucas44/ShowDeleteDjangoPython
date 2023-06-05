# members/models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField(default=0)