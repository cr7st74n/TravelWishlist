from django.shortcuts import render
from .models import Place

# Create your views here.

def place_list(request):
    places = Place.objects.all()   # we can change what we want to see by using a filter Ex : filter(visited=False)
    return render(request, 'travel_wishListCris/wishlist.html', {'places': places})