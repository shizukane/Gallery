from django.shortcuts import render, redirect
from .models import Location, Image, Category
from django.http import Http404

def index(request):
    '''
    view function to display landing page
    '''
    images = Image.objects.all()

    return render(request, 'index.html', {'images': images})

def search_page(request):
    '''
    view function to open search page and display searched images
    '''

    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        images = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'images': images})

    else:
        message = 'Please enter a term to be sought for'
        return render(request, 'search.html', {'message': message})

def sort_by_locations(request):
    '''
    View function to display images sorted location
    '''

    images = Image.filter_by_location()
    return render(request, 'location.html', {'images': images})

def single_image(request, image_id):
    '''
    view function to display a single image and details
    '''

    image = Image.get_image_by_id(image_id)
    return render(request, 'single_image.html', {'image': image})

    