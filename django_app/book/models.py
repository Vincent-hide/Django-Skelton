from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.IntegerField()
    publishedDate = models.DateTimeField(auto_now_add=True)
