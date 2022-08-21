from django.db import models

# Create your models here.
from django.urls import reverse
from django.template.defaultfilters import slugify # new

class Success_Stories(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True)  # new

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'



    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)