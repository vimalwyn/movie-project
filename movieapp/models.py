from django.db import models

# Create your models here.
class Movie(models.Model):
    objects = None
    Name=models.CharField(max_length=250)
    Description=models.TextField()
    Year=models.IntegerField()
    Image=models.ImageField(upload_to='gallery',)

    def __str__(self):
        return self.Name