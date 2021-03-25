from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='store')
    location = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name 
