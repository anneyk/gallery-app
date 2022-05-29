from unicodedata import category
from django.db import models

# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=50, unique='True')
  
  class Meta:
    ordering = ["location_name"]
    verbose_name = "Location"
    verbose_name_plural = "Locations"

  def __str__(self):
    return self.location_name

  def save_location(self):
    self.save()

  def delete_location(self):
    self.delete()

class Category(models.Model):
  category_name = models.CharField(max_length=50, unique='True')
  
  def __str__(self):
    return self.category_name

  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()

  class Meta:
    ordering = ["category_name"]
    verbose_name = "Category"
    verbose_name_plural = "Categories"

class Image(models.Model):
  image = models.ImageField(upload_to = 'images/',null=True)
  image_name = models.CharField(max_length=50)
  image_description = models.TextField(null=True)
  image_location = models.ForeignKey(Location, related_name='location', on_delete=models.DO_NOTHING,null=True)
  image_category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING,null=True)
  published_date = models.DateTimeField(auto_now_add=True, null=True)

  class Meta:
    ordering = ["published_date"]
    verbose_name = "Image"
    verbose_name_plural = "Images"

  def save_image(self):
    self.save()
  
  def delete_image(self):
    self.delete()