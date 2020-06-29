from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search_page'),
    path('locations/sorted/', views.sort_by_locations, name='sort_by_locations'),
    path('image/<image_id>/', views.single_image, name= 'single_image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)