from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    if request.method == 'POST':
        #create a new place
        form = NewPlaceForm(request.POST) # creating a form from data in the request 
        place = form.save() # createing a new model object from form
        if form.is_valid(): # validation againts DB constaints
            place.save()  #saves place to db
            return redirect('place_list')  # reloads home page 


    places = Place.objects.filter(visited=False).order_by('name')   # we can change what we want to see by using a filter Ex : filter(visited=False)
    new_place_form = NewPlaceForm()   # used to create HTML
    return render(request, 'travel_wishListCris/wishlist.html', {'places': places, 'new_place_form': new_place_form})