from django.db import models
from django.utils import timezone

class Toy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Finch(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    habitat = models.TextField()
    toys = models.ManyToManyField(Toy, blank=True)

    def __str__(self):
        return self.name

class Feeding(models.Model):
    feeding_date = models.DateField(verbose_name='Feeding Date', default=timezone.now)
    food_type = models.CharField(max_length=100, verbose_name='Food Type')
    notes = models.CharField(max_length=255, verbose_name='Notes')
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name='feedings')

    def __str__(self):
        return f"{self.finch.name} - {self.feeding_date}"