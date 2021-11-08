from django.db import models

# Create your models here.


class Book(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, default="https://iajw.org/wp-content/uploads/2019/09/What-is-journal-writing-image-of-blank-journal.jpg")
    rating = models.FloatField()
    description = models.CharField(max_length=800)
    category = models.CharField(max_length=200)