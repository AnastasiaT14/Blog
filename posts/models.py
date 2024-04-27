from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField()


