from django.db import models
from cloudinary.models import CloudinaryField
class Image(models.Model):
    image = CloudinaryField('image')
    description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-updated', '-created']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,pk):
        return cls.objects.get(id=pk)

    @classmethod
    def get_image_by_id(cls,pk):
        return cls.objects.get(id=pk)

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

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()