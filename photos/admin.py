from django.contrib import admin
from .models import Location, Category, Image

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
  list_display = ['location_name']
  ordering = ['location_name']

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['category_name']
  ordering = ['category_name']

class ImageAdmin(admin.ModelAdmin):
  list_display = ['image_name','image_description','image_category','image_location','published_date']

admin.site.register(Location,LocationAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Image,ImageAdmin)