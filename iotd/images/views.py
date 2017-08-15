from django.shortcuts import render_to_response
from images.models import FeaturedImage
from django.conf import settings
from django.http import Http404

def home(request):
    try:
        image = FeaturedImage.objects.latest('uploaded') 
        print(settings.STATIC_ROOT)
        return render_to_response('images/home.html',
                                  { 'image' : image})
    except FeaturedImage.DoesNotExist:
        raise Http404('No %s matches the given query.' % FeaturedImage._meta.object_name)
