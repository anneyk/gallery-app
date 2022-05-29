from django.test import TestCase
from .models import Location, Category, Image

class LocationTestClass(TestCase):
  #set up method
  def setUp(self):
    self.loc1 = Location(location_name = 'Nairobi')
  #testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.loc1, Location))

class CategoryTestClass(TestCase):
  def setUp(self):
    self.cat1 = Category(category_name = 'Travel')
   
  def test_instance(self):
    self.assertTrue(isinstance(self.cat1, Category))

class ImageTestClass(TestCase):
  def setUp(self):
    self.img1 = Location(location_name = 'Nairobi')
    self.img1.save_location()

    self.new_image = Image(image_name = 'Kisumu', image_description = 'This is a trip to Kisumu', image_location = self.img1)

    self.new_image.save()

    def test_instance(self):
      self.assertTrue(isinstance(self.new_image, Image))