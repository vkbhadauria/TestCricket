from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Address(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    house_no = models.CharField(max_length=254)
    locality = models.CharField(max_length=254)

    def __str__(self):
        return self.locality
