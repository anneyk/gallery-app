from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$',views.index,name= 'index'),
  url(r'^gallery/$', views.gallery, name = 'gallery'),
  url(r'^gallery/<int:image_id>/$', views.image_description, name='img_description'),
  url(r'^categories/travels/$', views.travels, name = 'travels'),
  url(r'^categories/birds/$', views.birds, name = 'birds'),
  url(r'^categories/anime_characters/$', views.anime_characters, name = 'anime_characters'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)