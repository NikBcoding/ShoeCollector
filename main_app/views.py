from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe

# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

# Create your views here.
def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', {
        'shoes': shoes
    })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    return render(request, 'shoes/detail.html', {
        'shoe': shoe
    })

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = '__all__'
    # "if you want specific fields to be updated"
    # fields = ['brand','name', 'style', 'description']


class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'