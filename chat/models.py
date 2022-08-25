from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(max_length=2000)

    def __str__(self):
        return self.text[:50]
