from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_category = models.ForeignKey(Category)
    image_location = models.ForeignKey(Location)

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        photos=cls.objects.filter(image_category__name__contains=search_term)
        return photos
