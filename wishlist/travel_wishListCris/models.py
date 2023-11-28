from django.db import models

# Create your models here.   Our class Place will have a name, and a visited boolean value
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} visited {self.visited}'
    