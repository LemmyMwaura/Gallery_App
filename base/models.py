from django.db import models
from cloudinary.models import CloudinaryField
class Image(models.Model):
    image = CloudinaryField('image')
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-updated']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image():
        pass

    def get_image_by_id(self,id):
        return self.objects.get(id=id)

    @classmethod
    def search_image(cls,category):
        return cls.objects.filter(category__name__icontains=category)

    @classmethod
    def filter_by_location(cls,location):
        return cls.objects.filter(location__name__icontains=location)

class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
