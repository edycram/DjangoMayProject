from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request,'htmlfile',context)