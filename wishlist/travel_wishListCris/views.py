from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    if request.method == 'POST':
        #create a new place
        form = NewPlaceForm(request.POST) # creating a form from data in the request 
        place = form.save() # creating a new model object from form
        if form.is_valid(): # validation against DB constraints
            place.save()  #saves place to db
            return redirect('place_list')  # reloads home page 


    places = Place.objects.filter(visited=False).order_by('name')   # we can change what we want to see by using a filter Ex : filter(visited=False)
    new_place_form = NewPlaceForm()   # used to create HTML
    return render(request, 'travel_wishListCris/wishlist.html', {'places': places, 'new_place_form': new_place_form})

def places_visited(request):
    visited = Place.objects.filter(visited=True).order_by('name')
    return render(request, 'travel_wishListCris/visited.html',{'visited':visited})

def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place ,pk = place_pk)
        place.visited = True
        place.save()
    return redirect('places_visited') # we can redirect to any URL


def  about(request):
    author = 'Cristian'
    about = 'This webpage is used to create a list of places that you could visite or that may be an option to visit'
    return render(request, 'travel_wishListCris/about.html',{'author':author,'about':about})

