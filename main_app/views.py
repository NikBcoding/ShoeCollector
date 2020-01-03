from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Shoe, Store
from .forms import CleaningForm

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
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', {
        'shoe': shoe,
        'cleaning_form': cleaning_form
    })

class ShoeCreate(CreateView):
    model = Shoe
    fields = ['brand', 'name', 'style', 'description']

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['brand', 'name', 'style', 'description']
    # "if you want specific fields to be updated"
    # fields = ['brand','name', 'style', 'description']


class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'

def add_cleaning(request, shoe_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.shoe_id = shoe_id
        new_cleaning.save()
    return redirect('detail', shoe_id=shoe_id)


def assoc_store(request, shoe_id, store_id):
  Shoe.objects.get(id=shoe_id).store.add(store_id)
  return redirect('detail', shoe_id=shoe_id)

def unassoc_store(request, shoe_id, store_id):
  Shoe.objects.get(id=shoe_id).store.remove(store_id)
  return redirect('detail', shoe_id=shoe_id)

class StoreList(ListView):
  model = Store

class StoreDetail(DetailView):
  model = Store

class StoreCreate(CreateView):
  model = Store
  fields = '__all__'

class StoreUpdate(UpdateView):
  model = Store
  fields = ['name', 'location']

class StoreDelete(DeleteView):
  model = Store
  success_url = '/stores/'