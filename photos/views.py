from django.shortcuts import render
from .models import Image,Category,Location

from django.http  import HttpResponse
# Create your views here.
def index(request):
    images = Image.objects.all()
    locations=Location.objects.all()
    return render(request,'index.html',{'images':images,'locations':locations})

def search_category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = (request.GET.get('category')).title()
        searched_images = Image.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'images':searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request,'search.html',{'message':message})

def display_location(request,location_id):
    try:
        locations = Location.objects.all()
        location = Location.objects.get(id = location_id)
        images = Image.objects.filter(image_location = location.id)
    except:
        raise Http404()
    return render(request,'location.html',{'location':location,'images':images,'locations':locations})
        
