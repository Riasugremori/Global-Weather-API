from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)  
    temperature = models.CharField(max_length=200, null=True, blank=True)  
    humidity = models.FloatField(null=True, blank=True)
    description = models.TextField 

    def __str__(self):
        return self.name
