from django.shortcuts import render
# Add the following import
class Shoe:
    def __init__(self, brand, name, style, description):
        self.brand = brand
        self.name = name
        self.style = style
        self.description = description

shoes = [
    Shoe('Adidas', 'NMD', 'running', 'sick!')
    ]

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    return render(request, 'shoes/index.html', {
        'shoes': shoes
    })
# Create your views here.
