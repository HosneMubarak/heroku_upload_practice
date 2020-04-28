from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name
