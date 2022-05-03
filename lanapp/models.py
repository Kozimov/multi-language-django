from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    
    def __str__(self):
        return str(self.name)