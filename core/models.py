from django.db import models

class Book(models.Model):
    tittle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.FloatField()


    def __str__(self):
        return f"{self.tittle} - {self.author}"
