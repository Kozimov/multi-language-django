from django.db import models
from django.urls import reverse


class Info(models.Model):
    class Meta:
        verbose_name = "Malumot"
        verbose_name_plural = "Malumotlar"


    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("lanapp:info", kwargs={'slug': self.slug})