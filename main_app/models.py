from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    habitat = models.TextField()
    # Add more attributes as needed

    def __str__(self):
        return self.name
