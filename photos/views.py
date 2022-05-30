from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Location, Category, Image
# Create your views here.
def index(request):
  gallery = Image.objects.all()[:6]
  return render(request,'index.html',{'gallery':gallery})

def image_description(request,image_id):
  image_descr = get_object_or_404(Image, pk=image_id)
  return render(request,'img_description.html',{'image_descr':image_descr})

def search_category(request):
  if 'category' in request.GET and request.GET["category"]:
    search_term  =  request.GET.get("category")
    searched_images = Image.search_by_category(search_term)
    message  = f"{search_term}"
        
    return render(request, 'search.html', {"message":message, "images":searched_images})
  else:
    message = "You have not searched for any category"
        
    return render(request, 'search.html', {"message":message})

def gallery(request):
  gallery = Image.objects.all()
  return render(request, 'gallery.html', {"gallery":gallery})

def travels(request):
  travels_category = Category.objects.get(pk=1)
  travels = Image.objects.all().filter(category=travels_category)
  return render(request,'categories/travels/travels.html',{"travels":travels})

def anime_characters(request):
  anime_characters_category = Category.objects.get(pk=1)
  anime_characters = Image.objects.all().filter(category=anime_characters_category)
  return render(request,'categories/anime_characters/anime_characters.html',{"anime_characters":anime_characters})

def birds(request):
  birds_category = Category.objects.get(pk=1)
  birds = Image.objects.all().filter(category=birds_category)
  return render(request,'categories/birds/birds.html',{"birds":birds})