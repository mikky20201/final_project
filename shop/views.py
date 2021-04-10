from django.shortcuts import render

from .models import Category, Product

# Create your views here.
def categories(request):
    return{
        'categories': Category.objects.all()
    }

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products':products})
