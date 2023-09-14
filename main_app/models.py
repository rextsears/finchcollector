from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    habitat = models.TextField()

    def __str__(self):
        return self.name

class Feeding(models.Model):
    finch = models.ForeignKey('Finch', on_delete=models.CASCADE, related_name='feedings')
    date = models.DateField()
    food_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.finch.name} - {self.date}"