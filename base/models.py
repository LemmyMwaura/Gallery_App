from django.db import models

# Create your models here.

class Image(models.Model):
    # Image = 
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # location Foreign Key =

    def __str__(self):
        return self.name