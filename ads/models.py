from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=3000)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)
